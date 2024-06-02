import asyncio
from telethon import errors
from functools import wraps


def exception_handler(async_func):
    @wraps(async_func)
    async def wrapper(*args, **kwargs):
        try:
            return await async_func(*args, **kwargs)
        except errors.FloodWaitError as e:
            print(f"Ошибка FloodWaitError: нужно подождать {e.seconds} секунд")
            await asyncio.sleep(e.seconds)
        except errors.PhoneNumberInvalidError:
            print("Ошибка: неверный номер телефона")
        except errors.SessionPasswordNeededError:
            print("Ошибка: необходим пароль для сессии")
        except errors.PhoneCodeInvalidError:
            print("Ошибка: неверный код телефона")
        except errors.PhoneCodeExpiredError:
            print("Ошибка: код телефона истек")
        except errors.MessageEmptyError:
            print("Ошибка: пустое сообщение")
        except errors.MessageTooLongError:
            print("Ошибка: сообщение слишком длинное")
        except errors.MessageNotModifiedError:
            print("Ошибка: сообщение не было изменено")
        except errors.UserNotMutualContactError:
            print("Ошибка: пользователь не является взаимным контактом")
        except errors.UserPrivacyRestrictedError:
            print("Ошибка: у пользователя включены ограничения конфиденциальности")
        except errors.ChatAdminRequiredError:
            print("Ошибка: необходимы права администратора чата")
        except errors.ChatWriteForbiddenError:
            print("Ошибка: запись в чат запрещена")
        except errors.TakeoutInitDelayError:
            print("Ошибка: задержка инициализации выноса данных")
        except errors.UserBannedInChannelError:
            print("Ошибка: пользователь забанен в канале")
        except errors.ChannelPrivateError:
            print("Ошибка: канал приватный")
        except errors.GroupedMediaInvalidError:
            print("Ошибка: недопустимое сгруппированное медиа")
        except errors.PeerIdInvalidError:
            print("Ошибка: неверный идентификатор пользователя")
        except errors.ChannelInvalidError:
            print("Ошибка: неверный канал")
        except errors.ChatIdInvalidError:
            print("Ошибка: неверный идентификатор чата")
        except errors.UserIdInvalidError:
            print("Ошибка: неверный идентификатор пользователя")
        except errors.MessageIdInvalidError:
            print("Ошибка: неверный идентификатор сообщения")
        except errors.RandomIdInvalidError:
            print("Ошибка: неверный случайный идентификатор")
        except errors.RandomIdDuplicateError:
            print("Ошибка: дублирование случайного идентификатора")
        except errors.EncryptionDeclinedError:
            print("Ошибка: шифрование отклонено")
        except errors.EncryptionAlreadyDeclinedError:
            print("Ошибка: шифрование уже отклонено")
        except errors.TimeoutError:
            print("Ошибка TimeoutError: истекло время ожидания")
        except errors.ConnectionError:
            print("Ошибка ConnectionError: ошибка подключения")
        except errors.RPCError as e:
            print(f"Произошла ошибка RPCError: {e}")
        except ValueError as e:
            print(f"Ошибка ValueError: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    return wrapper
