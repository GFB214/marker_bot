#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.
from text2image import CreateImg, DealText
from init import init
from marker import add_mark, add_mark_dir, gen_mark
import os, uuid
from werkzeug.utils import secure_filename
from contextlib import ExitStack

import logging
from telegram import Update, ForceReply, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

args = init()
mark = gen_mark(args)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def dealDocument(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    file_name = update.message.document.file_name
    file_name = uuid.uuid4().hex + "." + \
            secure_filename(file_name).split(".")[-1]
    imagePath = os.path.join(args.input, file_name)
    update.message.document.get_file().download(custom_path=imagePath)
    add_mark(imagePath, mark, args)
    resultPath = os.path.join(args.out, file_name)
    with open(resultPath,"rb") as file:
        update.message.reply_document(file)

def dealText(update: Update, _: CallbackContext) -> None:
    text = update.message.text
    text = DealText(text)
    text_images = CreateImg(text)
    for text_image in text_images:
        file_name = uuid.uuid4().hex + "." + "png"
        imagePath = os.path.join(args.input, file_name)
        add_mark_dir(text_image,imagePath,mark,args)
        resultPath = os.path.join(args.out, file_name)
        with open(resultPath,"rb") as file:
            update.message.reply_document(file)

def dealPhoto(update: Update, _: CallbackContext) -> None:
    photo = update.message.photo[-1]
    file_name = photo.get_file().file_path.split("/")[-1]
    file_name = uuid.uuid4().hex + "." + \
        secure_filename(file_name).split(".")[-1]
    imagePath = os.path.join(args.input, file_name)
    photo.get_file().download(custom_path=imagePath)
    add_mark(imagePath, mark, args)
    resultPath = os.path.join(args.out, file_name)
    with open(resultPath,"rb") as file:
        update.message.reply_document(file)


def main() -> None:
    updater = Updater(args.token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, dealText))
    dispatcher.add_handler(MessageHandler(Filters.document.image,dealDocument))
    dispatcher.add_handler(MessageHandler(Filters.photo,dealPhoto))


    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()