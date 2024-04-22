from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Keyboards.prof_keyboards import make_row_keyboard

router = Router()

available_directions_names = ["Хирургический центр", "Диагностический центр",
                              "Онкологический центр", "Отделение эндоскопии"]

available_services_names = ["Консультация", "Записаться на приём"]


class DirectionsNames(StatesGroup):
    directions_names = State()
    services_names = State()


#Хэндлер на команду /Направление
@router.message(Command('Направление'))
async def directions(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
        f'{name}, выбирайте направление: ',
        reply_markup=make_row_keyboard(available_directions_names)
    )
    await state.set_state(DirectionsNames.directions_names)


@router.message(DirectionsNames.directions_names, F.text.in_(available_directions_names))
async def services(message: types.Message, state: FSMContext):
    await state.update_data(services=message.text.lower())
    await message.answer(
        text='Спасибо, выбирайте услугу:',
        reply_markup=make_row_keyboard(available_services_names)
    )
    await state.set_state(DirectionsNames.services_names)
