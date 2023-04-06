# -*- coding: utf-8 -*-
import os
import PyPDF2

# 不斷請求使用者輸入存在的目錄
while True:
    directory = input("請輸入目錄名稱：")
    if os.path.exists(directory):
        break
    else:
        print("目錄不存在，請重新輸入。")

# 輸入密碼
password = input("請輸入 PDF 密碼：")

# 取得目錄下所有的 PDF 檔案
pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

# 逐一處理每一個 PDF 檔案
for pdf_file in pdf_files:
    # 開啟 PDF 檔案
    with open(os.path.join(directory, pdf_file), 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # 如果 PDF 檔案已經加密，就解密後存檔
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)

            # 建立 PdfFileWriter 物件，用來寫入解密後的內容
            pdf_writer = PyPDF2.PdfWriter()

            # 把每一頁的內容加到 PdfFileWriter 物件
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # 原始檔案更名
            os.rename(os.path.join(directory, pdf_file), os.path.join(directory, "orig_" + pdf_file))

            # 輸出解密後的 PDF 檔案
            with open(os.path.join(directory, pdf_file), 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"{pdf_file} 的密碼已清除，已另存為 {pdf_file}，原始檔案更名為 orig_{pdf_file}。")
        else:
            print(f"{pdf_file} 沒有加密，不需要解密。")

