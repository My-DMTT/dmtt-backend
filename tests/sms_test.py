from src.infrastructure.services.sms_service import SmsService

servic = SmsService()

servic.send_done_order_sms("998905360968", 5)
