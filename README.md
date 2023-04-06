# pdf-password-remover
A Python script for removing password protection from multiple PDF files in a directory

# 解密 PDF 檔案程式

這個 Python 程式可以處理指定目錄下所有被加密的 PDF 檔案，並解密它們。

## 使用方法

1. 在執行程式之前，確保已經安裝了 `PyPDF2` 模組。如果還沒有安裝，可以在終端機中輸入以下指令進行安裝：

~~~
pip install PyPDF2
~~~


2. 執行 `decrypt_pdf.py` 程式，程式會要求輸入目錄名稱和 PDF 檔案密碼。輸入正確的目錄名稱和密碼後，程式會開始處理所有被加密的 PDF 檔案。

~~~
python decrypt_pdf.py
~~~


3. 程式會逐一處理每一個被加密的 PDF 檔案，解密它們後儲存為同名檔案。原始檔案會被更名為 `orig_` 前綴。

~~~
XXX.pdf 的密碼已清除，已另存為 XXX.pdf，原始檔案更名為 orig_XXX.pdf。
~~~

如果 PDF 檔案沒有被加密，程式會顯示以下訊息：

~~~
XXX.pdf 沒有加密，不需要解密。
~~~


## 系統需求

- Python 3.6 或更新的版本。
- `PyPDF2` 模組。

## 注意事項

- 在解密 PDF 檔案之前，請確認您有合法的授權，並已取得檔案的密碼。
- 請勿使用這個程式來破解未經授權的 PDF 檔案。

## 作者

- 作者：ching-wei
