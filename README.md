# Project5-3_Hackthissite
# Hack This Site - Programming

## [Project3 GitHub](https://github.com/cislab-yzu/Project5-3_Hackthissite)

## 1053325 鐘偉豪 - Unscramble the words
### 題目
1. 從wordlist中隨機選出10組字串
2. 每個字串內的字母隨機排列
3. 請將上述產出的10組隨機排列的字串恢復原狀
4. 限時30秒!
![](https://i.imgur.com/Y9jPAHz.png)
### 解法
1. 網站有提供wordlist.txt，所以我們擁有全部的單字
2. 因為輸入值為隨機排列的，因此沒有順序性，為此我先將這些輸入值以ASCII來進行排列，排列之後依然不會是wordlist中的樣子，但是原本的隨機排列變成了依照ASCII排列
3. 同理，對wordlist做一樣的事，這樣input跟wordlist都是依照ASCII來進行排列了
4. 接下來只要比較輸入值跟wordlist是否一樣就好，如果一樣就把wordlist原本的字串加到結果中，最後將結果印出並貼到hack this site就完成了!
### 範例
![](https://i.imgur.com/7c2xAfc.png)
### 程式碼
```python=
f = open("wordlist.txt", "r")
wordlist = [line.strip() for line in f]
f.close()
candidate_list = list()

for candidate in wordlist:
	#print(candidate)
	sort_candidate = [c for c in candidate]
	sort_candidate.sort()
	candidate_list.append((sort_candidate, candidate))
print("enter the scrmable words")
input_str = list()
for i in range(10):
	string = input()
	sort_string = [c for c in string]
	sort_string.sort()
	input_str.append(sort_string)
result = list()
for i in input_str:
	for j in candidate_list:
		if i == j[0]:
			result.append(j[1])
print (','.join(result))
```
---

## 1051507 林益聖 - String manipulation
### 程式碼GitHub: [Code](https://github.com/Howieeee/HTS_Programming-Mission-12)
### 題目網址: [String manipulation](https://www.hackthissite.org/missions/prog/12/)

![](https://i.imgur.com/2ubIwKu.png)

1. 將題目給定的字串中字母與數字分開。
2. 設定數字皆為一位數且計算字串中所有質數和與所有非質數分開和的積 ( product )
3. 取字串中前25個字母並將其 ASCII value 加一（charList）
4. 最後 charList 與 product 連接形成答案
5. 答案格式: nc\$jdw$vx%o%puzznexeijzzt79926
6. 5秒內必須提交答案

### [Selenium Installation Tutorial](https://hackmd.io/Pc0Vxs3oRriemb31mRJneA)
### 解法 : 利用 Selenium 驅動瀏覽器操作網頁

### 程式碼
```python=
from selenium import webdriver #import selenium套件

driver = webdriver.Firefox() #開啟瀏覽器
driver.get('https://www.hackthissite.org/') #到達 HTS 官網
time.sleep(2) #緩衝一下 以免未完全load造成錯誤 (以下相同部分同理)

search_input = driver.find_element_by_name("username") #找到網頁user欄位
search_input.send_keys(info['user']) #輸入帳號
time.sleep(2)

search_input = driver.find_element_by_name("password") #找到網頁pwd欄位
search_input.send_keys(info['pwd']) #輸入密碼
time.sleep(2)

start_search_btn = driver.find_element_by_name("btn_submit") #找到登入按鈕
start_search_btn.click() #按下登入　
time.sleep(2)

driver.get('https://www.hackthissite.org/missions/prog/12/') #到達題目網站

allHtml = driver.page_source #取得題目網站html內容


startPos = str(allHtml).find("String:") #找尋String欄位
endPos = str(allHtml).find("<form")

targetStr = allHtml[startPos+38:endPos-17] #根據網頁內容位移取得單純字串內容

print('str ' + str(targetStr))

numList, charList = numOrChar(targetStr) #判斷字串內數字&字元

numberProduct = calPrime(numList) #計算(質數和)*(非質數和)

shiftedString = shift_ascii(charList) #計算前25個字元 ASCII code + 1 的結果

ans = shiftedString + str(numberProduct) #串接形成答案

ansInput = driver.find_element_by_name("solution") #找到答案欄位
ansInput.send_keys(str(ans)) #輸入答案

submitBtn = driver.find_element_by_name("submitbutton") #找到submit按鈕
submitBtn.click() #submit
```

---
## 1051446 游采蓉 - Parse an XML file 
### 題目 
登入Hack This Sit 後可查看題目[Parse an XML file](https://www.hackthissite.org/missions/prog/4/)


 ![](https://i.imgur.com/ECwUg57.png)
 >第一個here可下載解壓縮bz2
 >第二個here是[題目講解](https://www.hackthissite.org/missions/prog/4/info.html)
----
### 題目講解
讀取xml內的資訊，最後能夠透過直線和圓弧，畫出多個數字及字母。
![](https://i.imgur.com/BKrwAvL.png)

### 解題流程
1. 解壓縮bz2得到xml檔案
2. 使用php讀取xml內的資料
3. 繪製（把所有的直線還有圓弧都畫出來）
4. 輸出圖檔
5. 點開圖檔依序找出「藍,綠,紅,黃,白」五種顏色的數字和字母輸入答案
### CODE
```php=
<?php
header("Content-type: image/png");
$xml=simplexml_load_file("./plotMe.xml");
$png=@imagecreatetruecolor(600, 600)or die("failed to export image!");

// parse the line
foreach($xml->Line as $line){
	$XStart = (double)($line->XStart);
	$YStart = (double)($line->YStart);
	$XEnd = (double)($line->XEnd);
	$YEnd = (double)($line->YEnd);
	
	$Color = 'white'; //defult color
	$ColorVal = 0; 

	if(isset($line->Color)){
		$Color = $line->Color;
	}

	if($Color == 'red'){
		$ColorVal = imagecolorallocate($png, 255, 0, 0);
	}
	elseif($Color == 'green'){
		$ColorVal = imagecolorallocate($png, 0, 255, 0);
	}
	elseif($Color == 'blue'){
		$ColorVal = imagecolorallocate($png, 0, 0, 255);
	}
	elseif($Color == 'yellow'){
		$ColorVal = imagecolorallocate($png, 255, 255, 0);
	}
	else{
		$ColorVal = imagecolorallocate($png, 255, 255, 255);
	}
	//draw the line 
	imageline($png, $XStart, 600-$YStart, $XEnd, 600-$YEnd, $ColorVal);
} 

// parse the Arcs
foreach($xml->Arc as $arc){
	$width = (double)($arc->Radius)*2;
	$XCenter = (double)($arc->XCenter);
	$YCenter = (double)($arc->YCenter);
	$ArcStart = (int)($arc->ArcStart);
	$ArcExtend = (int)($arc->ArcExtend);

	$Color = 'white';
	$ColorVal = 0;

	if(isset($arc->Color))
		$Color = $arc->Color;

	if($Color == 'red'){
		$ColorVal = imagecolorallocate($png, 255, 0, 0);
	}
	elseif($Color=='green'){
		$ColorVal=imagecolorallocate($png,0,255,0);
	}
	elseif($Color=='blue'){
		$ColorVal=imagecolorallocate($png,0,0,255);
	}
	elseif($Color=='yellow'){
		$ColorVal=imagecolorallocate($png,255,255,0);
	}
	else{
		$ColorVal=imagecolorallocate($png,255,255,255);
	}
	//draw
	imagearc($png,$XCenter,600-$YCenter,$width,$width,360-($ArcStart+$ArcExtend),360-$ArcStart,$ColorVal);
}
imagepng($png);
imagedestroy($png);
?>

```
### run
```
$ php ProgrammingMission4.php > p4.png
$ open p4.png
```
### 結果圖檔參考
![](https://i.imgur.com/wCMJ4aT.png)
依序輸入Answer: 
0D7,072,F8D11B9CA6,5BAF65AF8B,AA2C12A42E

(blue, green, red, yellow, white)
### Reference
[Hack This Site Programming 4](https://www.youtube.com/watch?v=DIw9GXjosZc)

---

