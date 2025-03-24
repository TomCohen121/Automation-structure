import time
from pages.base_page import BasePage
from playwright.sync_api import Page


class Messages(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

    # --------------------------- Create Message Locators ---------------------------
   def btn_plus_new_message(self):
      return self.page.locator(".messagesBar-title button")

   def dropdown_recipient_selection(self):
       return self.page.locator('input[placeholder="חפש כאן..."]')

   def checkbox_choose_recipient(self, recipient):
       return  self.page.get_by_label(recipient).check()

   def btn_choose_recipient_dropdown_options(self):
       return self.page.get_by_role("button", name="בחר")

   def field_message_header(self):
       return self.page.locator(".newMessageBody textarea")

   def field_message_body(self):
       return self.page.locator(".rich-editor-wrapper quill-editor p")

   def btn_send_message(self):
       return self.page.locator(".submitWrapper app-big-button")

   def btn_approve_send_message(self):
       return self.page.get_by_role("button", name="אישור")

   def btn_close_success_popup(self):
       return self.page.get_by_role("button", name="סגור")

   def btn_upload_file(self):
       return self.page.locator(".additional_Text")

    # --------------------------- Exists Message Locators ---------------------------

   def btn_first_message(self):
       return self.page.locator(".rx-virtual-scroll__runway.rx-virtual-scroll-element div").nth(1)

   def txt_incoming_message_headline(self):
       return self.page.locator(".incoming-message-popup.ng-star-inserted .message_headline").text_content().strip()

   def txt_incoming_message_body(self):
       return self.page.locator(".incoming-message-popup.ng-star-inserted .message_content").text_content().strip()

   def txt_incoming_message_sender(self):
       return self.page.locator(".incoming-message-popup .user-details p").first.text_content().strip()
