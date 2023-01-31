from aiogram import Router, F
from aiogram.filters import Command

from bot.db import Role
from bot.filters import RoleCheckFilter
from bot.utils.administrator.callback_data_factories import AdministratorCallback, AdministratorAction
from .administrator_panel import administrator_panel, button_administrator_panel

# Создание маршрутизатора
router = Router()

# Регистрация фильтров
router.message.filter(RoleCheckFilter(Role.ADMINISTRATOR))

# Регистрация обработчиков
router.message.register(administrator_panel, Command('administrator_panel'))
router.callback_query.register(button_administrator_panel,
                               AdministratorCallback.filter(F.action == AdministratorAction.FUTURE))

# Псевдоним
administrator_router = router
