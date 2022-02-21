QUETION=["松尾美和子が好きな男の名前は？","敬之が今勉強しているほんの著者は？","今日の夕飯は？"]
R_ANS=["敬之","寺倉修","あんこう鍋"]
HINT=["ゴボウが好きで漢字2文字","背表紙読んで！","海底の生き物の鍋　○○○う鍋！"]
for i in range(3):
      print(QUETION[i])
      ans=input()
      if ans == R_ANS[i]:
          print("正解です")
      else:
          print("不正解です");
          print("ヒント！")
          print(HINT[i])
          ans=input()
          if ans == R_ANS[i]:
              print("正解です")
          else:
              print("不正解です");
              print("やる気出して！！次！")
