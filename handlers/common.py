from aiogram import types, F, Router
from aiogram.filters.command import Command

from Keyboards.keyboards import kb1, kb2
from Keyboards.prof_keyboards import make_row_keyboard
from handlers.directions import available_directions_names

router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Добрый день, какой у Вас вопрос?', reply_markup=kb1)

#
# #Хэндлер на команду /stop
# @router.message(Command('stop'))
# async def cmd_stop(message: types.Message):
#     name = message.chat.first_name
#     await message.answer(f'Пока, {name}')


