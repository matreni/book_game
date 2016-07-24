# 451-500

#451 - можно выйти

d = {
	451:{
		'text' : """ Вы открываете сосуд, и комната наполняется неизвестным зеленоватым газом.
		К счастью, он не ядовит и быстро рассеивается.
		Однако теперь очевидно, что брать сосуд с собой не имеет ни малейшего смысла.
		Что вы сделаете дальше: возьмете стеклянный сосуд (253) или выйдете из комнаты (39)?  """,
		'goto':[253 , 39]
	},
	452:{
		'text':"""Вы спускаетесь по лестнице. 
		Она заканчивается дверью, которую вы осторожно открываете - 10. """,
		'goto':[10]	
	},			
	453:{
		'text':"""К счастью, разбойники поверили вам и соглашаются пропустить, не только ничего не взяв, но и любезно преподнеся на прощание перо аиста (- 28). Их предводитель не сомневается, что оно может пригодиться в дороге.
		Пока вы приходите в себя после пережитого, разбойники бесшумно скрываются в лесу. 
		А вам надо решать, куда направиться дальше, ведь вы так растерялись, что забыли спросить их об этом - 46.""",
		'goto' : [28,46]
	},
	454:{
		'text':""" Путь свободен. Теперь вы можете двигаться дальше. 
		Из-за деревьев виднеется мрачный замок, сторожевые башенки по бокам внимательно наблюдают за дорогой. 
		Ворота смотрят прямо на вас, и видно, что они охраняются. 
		Пойдете прямо к ним (319) или налево по лесу, в обход замка, надеясь проникнуть в него более легко (232)?""",
		'goto': [319,232]
	},
	455:{
		'text':""""Трое из Эвенло", - говорите вы старику. Он непонимающе смотрит на вас. "Трое из Эвенло", - повторяете вы. 
		Некоторый проблеск понимания появляется на его лице. 
		"Сейчас я принесу то, что вам нужно", - слышится в конце концов в ответ и библиотекарь скрывается за стеллажами - 645. """,
		'goto': [645]
	},
	456:{
		'text':"""Вы отдаете деньги, и проводник с радостью прячет их в небольшой сундучок, стоящий в углу. После этого вы с ним выходите из дома, проходите через сад и углубляетесь в лес.
		 По дороге ваш спутник весело болтает: у него подозрительно хорошее настроение.
		 Впрочем, наверно, ему нечасто удается подзаработать в такой глухомани - 637.  """,
		 'goto':[637]
	},
	457:{
		'text':"""У вас в руках амулет с зашитой внутри медвежьей шерстью.
		 Один раз за все путешествие с его помощью сможете позвать медведицу, чтобы она помогла победить врага. Ее Ловкость - 8, а Сила - 10. Она будет драться с вашим врагом по тем же правилам, по которым сражается Копия, и, победив его, вернется обратно в берлогу. Если она погибнет, принимать эстафету придется вам.
		 Амулетом можно воспользоваться в любом бою, но только за пределами Черного замка. Там амулет бессилен.
		 Поблагодарив медведицу, вылезаете из берлоги и идете дальше по дороге, уходящей с поляны в лес - 44.  """,
		 'goto':[44]
	},
	458:{
		'text':"""Старуха подбирает монеты, кланяется и растворяется в воздухе. Но перед вами две двери.
		 В какую из них вы пойдете: в противоположную от входа (252) или в ту, что справа (542)? """,
		 'goto':[252,542]
	},
	459:{
		'text':"""Открыв дверь, попадаете в просторную комнату. На этот раз перед вами гарем волшебника.
		 Жены чародея с удивлением смотрят на вас, но по их лицам не совсем понятно, насколько часто Зеленые рыцари заходят в эти покои.
		 Всего несколько секунд вы можете потратить на то, чтобы оглядеться. Ковры и зеркала, удобные
		 мягкие диваны, картины в золотых рамах - это самая богатая комната из всех, что вы встречали. Скорее всего Барлад Дэрт редко выходит из своего кабинета, поэтому в других помещениях вам встречалось только самое необходимое.
		 Но здесь он, несомненно, бывает часто. В гостиной есть еще одна дверь в противоположной стене.
		 Теперь решайте: пройдете через комнату и пойдете дальше по коридору, ни слова не сказав и надеясь, что Зеленый рыцарь имеет право это сделать (251), или поговорите с женщинами (157)?""",
		 'goto':[251,157]
	},
	460:{
		'text':"""Вы показываете заключенному серебряный свисток. Он подходит ближе к решетке и рассказывает о том, что когда-то был камердинером мага, а серебряный свисток - символ его должности. 
		Свисток украли, и разгневанный волшебник бросил его в темницу. Камердинер умоляет вернуть ему свисток. Сделаете это (587) или откажетесь и уйдете?
		Коридор заканчивается тупиком, так что в этом случае придется вернуться обратно на развилку и выбрать, двинетесь ли вы направо (537) или налево (348). """,
		'goto':[587,537,348]
	},
	461:{
		'text':"""По дороге, которую вы выбрали, долгое время идете без приключений. Начинает смеркаться.
		 Хотите поискать себе убежище на ночь (340) или продолжите свой путь при свете луны (442)? """,
		 'goto':[340,442]
	},
	462:{
		'text':"""Дорога все больше отклоняется вправо. Если вы еще ориентируетесь в лесу, то без труда определите, в нужную сторону она идет или нет.
		 В конце концов выходите на небольшую поляну, от которой влево ведет какая-то тропинка. Вдруг что-то маленькое и серое в траве привлекает ваше внимание.
		 Видя, что это заяц, медленно подходите поближе. Если вы голодны, то можете попытаться поймать его и восстановить свои силы (178), если же нет - продолжайте свой путь (333).""",
		 'goto':[178,333]
	},
	463:{
		'text':"""Гоблин не успевает даже крикнуть. Быстрая реакция и ловкость не подвели вас, и меч пригвоздил врага к косяку.
		 Хотите войти в сторожку и иметь дело с остальными (158) или лучше не будете больше искушать судьбу и направитесь к высокому зданию в центре двора (308)?""",
		 'goto':[158,308]
	},
	464:{
		'text':'Вы говорите, что главная ваша цель - разбудить и освободить Принцессу. Услышав это, старичок вызывается вам помочь. Он предупреждает, что хочет дать один совет и один предмет, а еще один предмет обменять на что-то, что у вас, конечно же, есть. Пока не слишком понятно, но вы соглашаетесь: почему бы не послушать, что он предложит. Совет таков: "С большой высоты больнее падать. Напоследок держись поправее". Вам не очень ясен его смысл, но, быть может, когда-нибудь и станет понятно, что имелось в виду. Предметом оказывается шкура оленя (- 81). Старичок не объясняет ее предназначение, но говорит, что в замке она может пригодиться. Видя, что имеет дело с благодарным слушателем, он раскрывает самый главный секрет, который поначалу хотел оставить при себе. В замок можно войти через потайную дверцу. Она откроется, если нажать на третий камень слева от дверной ручки. Если когда-нибудь вы обнаружите в стене потайную дверцу, прибавьте 28 к номеру параграфа, на котором будете находиться - и проникнете в замок. И наконец, последний предмет - это перстень с великолепным бриллиантом. Но ценность его не в камне, говорит старичок, а в том, что он может открыть многие двери в замке. Однако за перстень старичок просит у вас любое заклятие. Если согласны на это, то 600, если же нет, то поблагодарите, возьмите шкуру оленя и уходите - 55. ',
		'goto':[81,28,600,55]
	},
	465:{
		'text':'Несколько соседних клеток пусты. Вы быстро проходите мимо них и выходите в узкий коридор - 140.',
		'goto':[140]
	},
	466:{
		'text':'Вам удается пересечь пустое пространство без потерь, если не считать того, что вы бьетесь головой о противоположную стенку. Стена продолжается, и вы идете вдоль нее дальше - 352.',
		'goto':[352]
	},
	467:{
		'text':'Вы попадаете в маленькую проходную комнатку и толкаете следующую дверь. Она не заперта, и вы попадаете в огромную ярко освещенную парадную залу. Догадаться о ее предназначении нетрудно. Это столовая. Огромный дубовый стол тянется от одного конца до другого, по краям стоят лавки. С торца стола на вас смотрит огромный пустой черный трон, украшенный короной. Но сейчас столовая пуста, и вы можете не торопясь оглядеть ее, если только не боитесь, что кто-нибудь войдет. У противоположной от входа стены - невысокий изящный буфет. В дальнем углу - люк. Из комнаты ведут четыре двери (кроме той, в которую вы вошли). Три из них в стене справа и одна - рядом со входом. Дверь за спиной, как обычно, намертво захлопывается. Что вы сделаете? Осмотрите буфет (25), люк (224) или трон (22)? Выйдете из столовой? Тогда через какую дверь: в той же стене, в которой был вход (427), или через одну из трех других - правую (398), левую (206) или среднюю (350)?',
		'goto':[25,224,22,427,398,206,350]
	},
	468:{
		'text':'Зеркальце нравится хозяйке гарема, но оно не настолько ценно, чтобы ради него женщина выдала вам какую-нибудь тайну. Однако она уходит в свою комнату и не мешает вам поговорить с женами мага, вернувшись на 255, или выйти из гарема в следующий коридор - 251.',
		'goto': [255,251]
	},
	469:{
		'text':'"Ты обманул меня, - рычит Лев. - И не знаешь нужных слов". Его сильная лапа наносит удар прежде, чем вы успеваете защититься (потеряйте 2 СИЛЫ). Теперь волей-неволей придется пробиваться мечом - вернитесь на 257 и сражайтесь.',
		'goto':[257]
	},
	470:{
		'text':'Вы кидаете Гарпии зеркальце, и чародей не может скрыть своего разочарования. Кто бы мог подумать, что такая уродина уползет в угол наслаждаться своим отражением и оставит вас в покое - 388.',
		'goto':[388]
	},
	471:{
		'text':'Вы срываете одно из перьев лука, и оно на ваших глазах превращается в черную стрелу (+ 55). Можете нарвать стрел еще и взять с собой столько, сколько захотите, однако учтите, что каждая будет занимать одно место в вашем заплечном мешке. После этого вы выходите из комнаты, не дожидаясь, пока в ней появится разъяренный садовник - 80.',
		'goto':[80]
	},
	472:{
		'text':'Осторожно приближаетесь к хрустальной кровати с правой стороны и склоняетесь над Принцессой. Но в этот момент в ногу пребольно вонзается что-то острое. Это металлический шип, которого вы не заметили. ПРОВЕРЬТЕ СВОЮ УДАЧУ. Если вы удачливы, то 588, если же нет, то 391.',
		'goto':[588,391]
	},
	473:{
		'text':'Вы поступили правильно с точки зрения здравого смысла, но забыли о том, что убивать сдавшихся в бою не слишком порядочно. Бог войны Темес недоволен вами: киньте кубик и зачеркните соответствующий квадрат УДАЧИ (если он уже зачеркнут, вам повезло). После этого вы переступаете через трупы Орков и входите в ворота - 100.',
		'goto':[100]
	},
	474:{
		'text':'Вы приподнимаете крышку большого сундука, но она вырывается из рук и со всей силой бьет по пальцам. Потеряйте 1 ЛОВКОСТЬ и 2 СИЛЫ. Хотите еще раз попробовать поднять крышку (644) или займетесь одним из двух других сундуков - средним (540) или маленьким (380)? А может быть, лучше уйти, вернувшись на параграф с описанием большой залы (39)?',
		'goto':[644,540,380,39]
	},
	475:{
		'text':'Вы достаете золотой апельсин и разрезаете его. После этого подносите одну из долек к губам Принцессы, и на них проливается несколько капель волшебного сока. Румянец появляется на ее щеках, девушка глубоко вздыхает и садится на кровати. Она сразу же вспоминает, что с ней произошло, и первым делом спрашивает, жив ли ее мучитель - Барлад Дэрт. Если волшебник еще жив, то 589, если же мертв, то 655.',
		'goto':[589,655]
	},
	476:{
		'text':'Заклятие действует, но... - 347.',
		'goto':[347] 
	},
	477:{
		'text':'Торговец мертв, и вы быстро осматриваете его лавку. После недолгих поисков находите 10 золотых. Кроме того, можете взять с собой любой товар, который он предлагал, но вы не купили. Загляните еще раз в параграф 176 и выберите то, что понравится. Но вы убили честного человека - киньте кубик и зачеркните соответствующий квадрат УДАЧИ (если он к этому времени уже зачеркнут, считайте, что вам крупно повезло). Теперь уходите - 106. ',
		'goto':[106]
	},
	478:{
		'text':'Дверь открывается. Перед вами широкий коридор, стены которого выкрашены в не слишком приятный для глаза грязно-черный цвет. Пойдете по нему (320) или вернетесь на 434 и выберете другую дверь? ',
		'goto':[320,434]
	},
	479:{
		'text':'Вы вспоминаете про серебряный сосуд, в который так и не заглянули. Быстро достаете его из заплечного мешка и готовитесь открыть. Однако Зеленый рыцарь умоляет этого не делать, разрешая пройти. Откроете крышку, несмотря на его уговоры (590), или достаточно того, что вы как следует напугали стража и теперь можете идти дальше (392)? ',
		'goto':[590,392]
	},
	480:{
		'text':'Вы оказываетесь в библиотеке. Все стены заставлены шкафами с книгами. Путь вам преграждают многочисленные стеллажи, между которыми петляет узкий проход. Откуда-то из книжных завалов выныривает и хозяин. Это старик с маленькими хитрыми глазками, прикрытыми круглыми очками в металлической оправе. Старичок очень сутулится и больше похож не на человека, а на одну из тех крыс, которых вы только что видели. Он не безумно любезно спрашивает, что вам здесь надо? Сохраняя полное спокойствие, отвечаете, что хотели бы что-нибудь почитать. Какую книгу вы попросите: о Зеленых рыцарях (45), о самом волшебнике (345), о Принцессе (208) или скажете, что вы передумали и уйдете из библиотеки (591)? А может быть, вы хотите что-то передать старичку?',
		'goto':[45,345,208,591]
	},
	481:{
		'text':'Вам удается скрыться от рыцаря, только убежав в глубь леса. Естественно, на коне он не сможет скакать за вами по такому бурелому. Но куда же идти дальше? Передвигаться наугад по бездорожью очень тяжело (потеряйте 2 СИЛЫ), но в конце концов вы выходите на какую-то дорогу - 60.',
		'goto':[60]
	},
	482:{
		'text':'Средний коридор не подводит вас. Вскоре он упирается в дверь, на которой вы видите герб волшебника: Черный замок на белом поле - 241.',
		'goto':[251]
	},
	483:{
		'text':"""Барлад Дэрт смотрит на ваше оторопевшее лицо, потом начинает хохотать. Это длится довольно долго - затянувшаяся пауза уже начинает надоедать. Неужели ничего нельзя сделать? В отчаянии вы бросаетесь на волшебника с голыми руками. Он настолько не ожидает этого, что даже не успевает встать из-за стола, но через несколько мгновений как рыба выскальзывает из ваших рук. "Ну что ж, - говорит он задумчиво, - придется тебя проучить. Я буду драться с тобой". В руках у него оказывается меч, клинок которого светится в полутьме кабинета.
      	БАРЛАД ДЭРТ
      	Ловкость 14 Сила 12
      	Если вам удается победить мага, то 169.""",
		'goto':[169]
	},
	484:{
		'text':'Увы, в сторожке нет ничего интересного. Пить брагу, которой угощались Гоблины, ни малейшего желания: стоит только ее понюхать, как уже ясно, что на пользу это не пойдет. На столе лежат стаканчик с костями (- 78) и вещи, на которые шла игра: бронзовый свисток (- 214), лист вендории (+ 67), 3 золотых и медный браслет (+ 223). Возьмите все, что понравилось. Времени и так уже потрачено более чем достаточно, и вы идете по направлению к высокому зданию в центре двора - 308. ',
		'goto':[308]
	},
	485:{
		'text':"""Быстрой походкой со взглядом безумным вы приближаетесь к возвышению,поэтому вас называют Гумным. Но к кровати можно подойти и справа, и слева. С какой же стороны это сделаете вы?
      Справа - 472.
      Слева - 275. """,
		'goto':[472,275]
	},
	486:{
		'text':'Повар отсылает поварят готовить обед и вытирает руки об фартук. Он не прочь поболтать, но подумали ли вы, о чем стоит с ним поговорить? Спросите про сундук в углу (570), попросите накормить вас (91) или расспросите о замке (295)? ',
		'goto':[570,91,295]
	},
	487:{
		'text':"""Первым нападает Орк с мечом, который расспрашивал вас. Если хотите, воспользуйтесь заклятием Копии.
      	ПЕРВЫЙ ОРК
      	Ловкость 10 Сила 6
      	Если убили его за три раунда атаки, то сражайтесь с двумя остальными, тем более что их Лояльность понизится от этого на две единицы. Если же нет, то через три раунда оставшиеся два Орка приходят на помощь своему предводителю, и вам придется биться с тремя сразу.
      	ВТОРОЙ ОРК
      	Ловкость 7 Сила 8 Лояльность 10
      	ТРЕТИЙ ОРК
      	Ловкость 7 Сила 8 Лояльность 10
      	Как только Лояльность любого из них станет равна 3, он бросит оружие и сдастся. В этом случае после окончания боя - 638. Если же все враги мертвы, а вы по счастливой случайности живы, то можете переступить через тела своих поверженных противников и войти в ворота - 100.""",
      	'goto':[638,100]
	},
	488:{
		'text':'Дракон с удивлением смотрит на перо аиста, которое вы достаете. Этот аист был его старым другом и погиб всего несколько недель назад от когтей орла. Дракону дорога память о друге, и он пропускает вас, взлетая с поляны и скрываясь за облаками - 454. ',
		'goto':[454]
	},
	489:{
		'text':'За левой дверью - узкий коридор. Затхлый неприятный воздух сразу навевает мысли о смерти, запустении, тлене. Коридор упирается в стену. Вы пришли в тупик. Но в правой стене две двери. Откроете правую (501) или левую (547)?',
		'goto':[501,547]
	},
	490:{
		'text':'Вы выходите на развилку. Дровосеки явно пришли с этой стороны, но по какой из дорог? Да и стоит ли вам выбирать дорогу, по которой они пришли? Решайте, куда вы пойдете: направо (38) или прямо (214)?',
		'goto':[38,214]
	},
	491:{
		'text':'ПРОВЕРЬТЕ СВОЮ УДАЧУ. Если вы удачливы, то 631, если же нет - 593. ',
		'goto':[631,593]
	},
	492:{
		'text':'"Ну, так я помогу тебе выбраться отсюда!" - радостно потирая руки, говорит старичок-лесовичок. И прежде чем вы успеваете отказаться от столь неожиданной "помощи", он делает взмах рукой и - все вокруг исчезает. Потом лес опять возникает, но перед вами уже совсем другое место, да и дороги никакой нет. Вы сидите на муравейнике на краю большой поляны, от которой идет единственная дорога. Вам ничего не остается, как встать, вытряхнуть муравьев из одежды и пойти по ней - 151. ',
		'goto':[151]
	},
	493:{
		'text':'В этот момент за дверью раздается топот кованых сапог. Волшебник мертв, но ведь его люди не знают об этом. Очевидно, он сумел незаметно подать сигнал тревоги. Вы оборачиваетесь, готовясь к бою, и принимаете боевую стойку, выставив меч вперед. Когда дверь распахивается, становится понятно, что врагов слишком много, - нападают сразу двенадцать Зеленых рыцарей во главе с Бароном. Двух из них удается убить, но силы слишком неравны. Только после того, как ваш труп будет унесен из кабинета подоспевшими Орками, они заметят, что их повелитель мертв, но вам это уже не поможет. Барлад Дэрт пал, жители Элгариола могут спать спокойно, но Король так и не увидит своей дочери. Ведь вы не успели помочь ей, а через несколько часов скрепляющие цитадель чары падут, Черный замок рассыплется, как карточный домик, и земля поглотит его вместе со спящей Принцессой... ',
		'goto':[1]
	},
	494:{
		'text':'Вы достаете меч и атакуете крыс, но клинок только тупится об камень. Вам остается лишь достойно принять смерть от укусов мерзких тварей. А цель была столь близка... ',
		'goto':[1]
	},
	495:{
		'text':'Вы протягиваете женщинам 6 золотых. Они поражены вашей щедростью и дают один маленький совет: побольше обращайте внимания на зеркала - они могут быть полезны не только женщинам. Киньте кубик и почистите соответствующий квадрат УДАЧИ. Когда вы увидите зеркало, которым захотите воспользоваться, вычтите 13 из номера параграфа, на котором вы тогда будете находиться. Теперь же, выслушав жен мага, выходите из гарема и идите по новому коридору - 251. ',
		'goto':[251]
	},
	496:{
		'text':'Это усыпальница королевских слуг. Им положен не пышный саркофаг, а лишь общая могила - рядом с могильной плитой видна большая рукоять, которая поднимает плиту, чтобы вновь умершего можно было положить к его собратьям. Если хотите попробовать взяться за рукоять и поднять плиты, то 639. Если нет, то знайте, что пронизывающее воздух напряжение не позволяет задерживаться: все в вас стремится прочь от этого места. Так что решайте, через какую дверь лучше выйти: через правую (547) или левую (501).',
		'goto':[639,547,501]
	},
	497:{
		'text':'Увидев у вас в руках золотое кольцо, рыцарь кланяется и пропускает вас - 648.',
		'goto':[648]
	},
	498:{
		'text':'Вы выбираете щит. Он поможет вам отражать вражеские удары (прибавьте себе 1 ЛОВКОСТЬ, даже если ваша изначальная ЛОВКОСТЬ не уменьшалась). Пока вы примериваете щит, дверь сама собой закрывается, и открыть ее вновь уже не удается - 300. ',
		'goto':[300]
	},
	499:{
		'text':"""Вы накладываете заклятие Огня, и возникший в воздухе огненный шар испепеляет расспрашивавшего вас Орка. Остаются двое: один в ужасе убегает в лес, бросив у ворот оружие, а второй принимает ваш вызов:
      ОРК
      Ловкость 7 Сила 8
      Если вы победили стража, можете войти в ворота - 48. """,
      	'goto':[48]
	},
	500:{
		'text':"""Вы храбро выпиваете жидкость. Это Микстура жизненных сил. Прибавьте себе 6 СИЛ и уходите из домика, пока Гоблины не вернулись - 416. """,
		'goto':[416]
	},
	501:{
		'text':"Дверь без труда открывается. За ней - широкая лестница с удобными деревянными перилами, которая ведет вниз - 434.",
		'goto':[434]
	}
}
