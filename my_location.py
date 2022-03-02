'''
不一样的地方 
bda_note 

特记
account_name(不能用空的来做),可能影响input_reject_reson
'''

# linked in url list
idz_list=[15,18,19,16]
# 主页第一个人
first_item='//*[@id="brandBand_1"]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr/td[3]/span/a'
# 主页第一个bda_note
first_item_bdanote='//*[@id="brandBand_1"]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/span'
# detail
detail_lo='//*[@id="detailTab__item"]'
# linked_in iframe
iframe_lo='//iframe[@class="content-frame LIDSalesNavigator LIDSalesNavigatorMemberProfileComponent"]'
# 编辑按钮
change_lo='//button[@class="test-id__inline-edit-trigger slds-shrink-none inline-edit-trigger slds-button slds-button_icon-bare"]'
# email
email_lo='//div/div/slot/records-record-layout-row[14]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/emailui-formatted-email-lead/emailui-formatted-email-wrapper/force-aura-action-wrapper/div/a'
# name
name_lo='//div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/div/div[2]/span/slot[1]/lightning-formatted-name'
# company
company_lo='//div/div/slot/records-record-layout-row[4]/slot/records-record-layout-item[1]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# leads status
leads_status_lo='//div/div/slot/records-record-layout-row[1]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# BDA_Notes,index=-1
BDA_Notes_lo='//div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# BDA_title
BDA_title_lo='//div/div/slot/records-record-layout-row[3]/slot/records-record-layout-item[1]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# rejected_reson
rejected_reson_lo='//div/div/slot/records-record-layout-row[6]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# recent,index=-1
recent_lo='//header/div[@class="slds-media__body"]/h2/span'
# rejected_details
rejected_details_lo='//div/div/slot/records-record-layout-row[7]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# account_name
account_name_lo='//div/div/slot/records-record-layout-row[5]/slot/records-record-layout-item[1]/div/div/div[2]/span/slot[1]/force-lookup/div/records-hoverable-link/div/a/slot/slot/span'
# leads_status_text
leads_Status_text='//div/div/slot/records-record-layout-row[1]/slot/records-record-layout-item[2]/div/div/div[2]/span/slot[1]/lightning-formatted-text'
# 错误提示框
email_error='//div/records-record-edit-error/div/div/div/strong'
# 重复错误提示框
re_error='//div/force-dedupe-content/div'
# leads_input 输入框
input_leads_Status='//div/div/slot/records-record-layout-row[1]/slot/records-record-layout-item[2]/div/span/slot/records-record-picklist/records-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div'
# move_on 输入框
input_move_on='//div/div/slot/records-record-layout-row[5]/slot/records-record-layout-item[2]/div/span/slot/records-record-layout-checkbox/lightning-input/div/span/input'
# bda_note 输入框
input_bda='//input[@name="BDA_Notes__c"]'
# reject_reson 输入框
input_reject_reson='//div/div/slot/records-record-layout-row[6]/slot/records-record-layout-item[2]/div/span/slot/records-record-picklist/records-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div'
# reject_detail 输入框
input_reject_detail='//div/div/slot/records-record-layout-row[7]/slot/records-record-layout-item[2]/div/span/slot/records-record-layout-base-input/lightning-input/div/input'
# email 输入框
input_email='//div/div/slot/records-record-layout-row[14]/slot/records-record-layout-item[2]/div/span/slot/lightning-input/div/input'
# save_button
save_button_lo='//flexipage-tab2/slot/flexipage-component2/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/records-form-footer/div/div/div/runtime_platform_actions-actions-ribbon/ul/li[2]/runtime_platform_actions-action-renderer/runtime_platform_actions-executor-lwc-headless/slot[1]/slot/lightning-button/button'
# close_button
close_button_lo='/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li[2]/div[2]/button'