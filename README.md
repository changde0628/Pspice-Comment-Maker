# 如何使用PSpice自動加註解工具

**Author : changde0628**

## 前提

這個工具是用Python3寫的，因此在使用前必須確定你的電腦有Python3的任何一個版本。
5/8更新 : 或使用提供的.exe檔，操作方法相同。

Python : https://www.python.org/downloads/

## 使用

下載檔案Pspice_Comment_Maker.py or .exe，下載在任何一個位置，但我會建議放在桌面。

按下電腦的Windows鍵加R鍵，會出現以下視窗，輸入cmd，按下確定(或Enter)。

接著打開你下載的Pspice_Comment_Maker.py or .exe，右鍵點選內容，你會看到位置，把它複製起來。

回到cmd 輸入 : cd /d <你剛剛複製的位置>，按下Enter。

接著你可以開始使用Pspice_Comment_Maker了，輸入 : Pspice_Comment_Maker.py or .exe <你要加上註解的程式碼(含檔名)>

例如: 將excerise1.cir加上註解，輸入 : Pspice_Comment_Maker.py excerise1.cir
若你使用的是.exe，輸入 : Pspice_Comment_Maker.exe excerise1.cir

Warning : .model指令必須寫成nmos(...) or pmos(...)，不可為nmos (...) 

空格請貼著變數不要有多餘的空格，且不用寫單位，例如10uF，請寫10u，若寫10uF，註解會變成10uFF

## 後記

Version1.0 : Update 2022/3/28

Version1.1 : Update 2022/3/29 修正lambda偵測錯誤

Version1.2 : Updata 2022/4/20 新增方波偵測和.AC指令

Version1.3 : Updata 2022/5/3 新增偵測Cgso,Cgdo指令

Version1.4 : Updata 2022/5/8 新增.exe
