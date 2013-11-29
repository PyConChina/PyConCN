#coding=utf8
from uliweb.i18n import ugettext_lazy as _

data = [

##############################################################################
#
#   珠海  讲师信息
#
##############################################################################
    {
        'fullname':_('Zoom.Quiet'),
        'nickname':_('大妈'),
        'company':_('金山网络'),
        'position':_('过程改进经理'),
        'desc':_('Python 中文社区创始人 / 管理员，热心于python社区的公益事业，大家熟知的社区"大妈"；OBP及蟒营工程设计者 /主持人；参与并主持各种线上 / 线下活动，主持编撰了《可爱的Python》；坚持用 Pythonic 感化国人进入 FLOSS世界进行学习 / 分享 / 创造！目前就职于金山软件。'),
        'avatar':'zhouqi.jpg',
        'speech':_('《再再再再谈文学化编程》'),
    },

    {
        'fullname':_('赖勇浩'),
        'nickname':_(''),
        'company':_('某彩票行业公司'),
        'position':_('技术总监'),
        'desc':_('从业 8 年多，曾从事客户端游戏、网页游戏的研发，最近一年构建、带领团队开发基于 Web 技术的互联网、电话、自助终端销售彩票管理系统；开发食品、药品溯源系统等。现在是第三次作为讲师参加 PyCon China，也是珠三角技术沙龙的创办人和组委之一'),
        'avatar':'laiyonghao.png',
        'speech':_('《论 Python 与设计模式》'),
        'speech_desc':_('动态语言不需要设计模式？设计模式与 Python 水火不容？来，听我谈谈 Python 需要设计模式的地方，来，听我说说怎么样编写 Pythonic 的设计模式代码。'),
        
    },

    {
        'fullname':_('翁伟'),
        'nickname':_('Wuvist'),
        'company':_('Zalora South East Asia'),
        'company_desc':_('是时尚与美妆零售商，总部设在新加坡，在印度尼西亚、马来西亚、文莱、菲律宾、泰国、越南以及中国香港等地区均有业务'),
        'position':_('软件架构师'),
        'desc':_('热爱美食的编程员，熟悉服务器端开发，喜欢折腾，.net转python再转php又开始转GO'),
        'avatar':'131126_wengwei_sg.png',
        'speech':_('《论使用Python开发推荐引擎的优越性》'),
        'speech_desc':_('适合使用python开发推荐引擎的场景介绍以及相应的工具推荐,'),
    },

    {
        'fullname':_('李路'),
        'nickname':_(' '),
        'company':_('Knewone.com'),
        'position':_('联合创始人和CTO'),
        'desc':_('是 Knewone.com 的联合创始人和CTO，毕业于北京大学电子学系，原新浪高级软件工程师，09年辞职开始创业旅程，曾联合创办了中国第一个轻博客网站宽岛（kuandao.com）。最感兴趣的事情是 Lean Startup, 网站产品设计， 以及学习各种奇葩的编程语言，最崇拜的人是 Paul Graham。'),
        'avatar':'131111_lilu.png',
        'speech':_('《Artisan & Artist》'),
        'speech_desc':_('做为程序员，我们在工作时经常担任工匠（Artisan）的角色，去实现别人设计好的产品，但有时候，我们也渴望像一个艺术家（Artist）那样去创作......其实，设计并没有那么难，如果能够为你的Library设计出好的API，为你的CLI工具设计出人性化的使用方法，你就有能力设计出简洁，清晰，流畅的图形化用户体验。这个演讲将打破程序员与设计师之间的鸿沟，描绘出Unix哲学与良好的UI设计间的共同之处，让程序员也可以去尝试设计，从Artisan走向Artist。'),
    },


    {
        'fullname':_('潘俊勇'),
        'nickname':_('老潘'),
        'company':_('易度云办公'),
        'position':_('创始人，CTO'),
        'desc':_('python老兵，国内python社区最早的布道者之一， 从经营开源社区到创业，至今未放下代码。2002年开始创办Zope中文社区，同时也是润普公司创始人。2007年转向互联网软件，推出易度云办公(everydo.com)，专注企业云端办公方案。'),
        'avatar':'panjunyong.jpg',
        'speech':_('《我经历的软件重构》'),
        'speech_desc':_('从开源软件zope/plone的重构，到易度办公平台发展过程中的重构，谈不同时机、不同策略的软件重构带来的利与弊，以及python语言对软件重构的帮助'),
    },


    {
        'fullname':_('王健'),
        'nickname':_('Beckie'),
        'company':_(''),
        'position':_('技术总监'),
        'desc':_('网游行业资深从业者，技术发烧友，丰富的Python经验，代表作品有《富甲西游》，《月光之城》等'),
        'avatar':'131125_wangjian.jpg',
        'speech':_('《用Python架设大型多人在线游戏服务端》'),
        'speech_desc':_('支持海量用户数据存储，海量用户在线，Python将如何发挥自己的特点 '),
    },

    {
        'fullname':_('揭光发'),
        'nickname':_('Jeff'),
        'company':_('广州图锐信息科技有限公司 '),
        'position':_('创始人兼CTO'),
        'desc':_('Jeff，原一介文科生，误入工科学堂。几年间创业迫使自己练得周身刀，但可惜木有一把是锋利的 >_< ！能写点python，略懂iOS客户端编程，能弹几首儿歌哄女儿睡觉，偶尔客串做下男声优。是珠三角技术沙龙组委兼现任主席，始终坚持奋战于代码前线。相信every one can code。 '),
        'avatar':'131123_jeff.png',
        'speech':_('《 使用sentry来管理你应用的异常及日志》'),
        'speech_desc':_(' 暂定Sentry相关的主题，视情况可能会调整。'),
    },

    {
        'fullname':_('黄毅'),
        'nickname':_('codeplayer'),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《Python性能优化实践》'),
    },

    {
        'fullname':_('刘宇'),
        'nickname':_('Martin Liu'),
        'company':_('ThoughtWorks'),
        'position':_('用户体验设计师'),
        'desc':_('是中国最早的TEDx活动TEDxUIC的发起人，在过去的3年里，组织及协助组织过多个TEDx活动，亦为多个TEDx策展团队的成立提供过辅导。刘宇是一个活跃的活动组织者、领导者，见证了TEDx中国社区的自我蓬勃发展!'),
        'avatar':'131126_martinliu.jpg',
        'speech':_('《TEDx社区自我繁荣的独特文化》'),
        'speech_desc':_('，在这次的演讲中，他将为大家带来TEDx社区多姿多彩的独特成长故事。刘宇现在在著名技术咨询公司ThoughtWorks担任用户体验设计师一职'),
    },


    {
        'fullname':_('StephanieYR'),
        'nickname':_(''),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《???》)'),
    },


##############################################################################
#
#   上海  讲师信息
#
##############################################################################

    {
        'fullname':_('陈世欣'),
        'nickname':_('Sting Chen'),
        'company':_('永泰红磡养老产业投资集团'),
        'position':_('信息技术总监'),
        'desc':_('在14年的互联网生涯后，投身到到永泰红磡养老产业投资集团做夕阳事业，跨界发展。他是TopGeek技术社区的创办人也是上海GDG的负责人，并参与CPyUG社区的管理。还发起PMCamp产品经理社区，儿童社区乐创园等。'),
        'avatar':'chenshixin_2013.png',
        'speech':_('大会致辞《一个神奇的语言》'),
    },


    {
        'fullname':_('杜玉杰'),
        'nickname':_('Ben'),
        'company':_('OpenStack'),
        'position':_('OpenStack基金会董事'),
        'desc':_('他在中国组织了许多OpenStack开源社区的工作，从小聚会的大型会议，如PyCon中国，社会管理器事件，中国云连接（C3）2011年上海OpenStack的首脑会议，OpenStack沙龙，2012亚洲OpenStack的的会议等。也是九州云的社区发展总监。'),
        'avatar':'ben-duyujie.jpg',
        'speech':_('CodeLab:用OpenStack快速实现私有云，搭建自动化运维体系'),
    },

    {
	    'fullname':_('洪强宁'),
		'nickname':_('洪教授'),
		'company':_('豆瓣'),
		'position':_('豆瓣首席架构师'),
		'desc':_('豆瓣第一位全职员工。清华毕业后，洪强宁一直做嵌入式系统。在2002年开始接触Python语言，从硬件工程师变为软件工程师，对一种语言在计算机底层如何工作有深入的理解。'),
		'avatar':'???.jpg',
		'speech':_('《DAE系统的设计》'),
	},


    {
	    'fullname':_('叶剑烨'),
		'nickname':_('Ryan Ye'),
		'company':_('Glow'),
		'position':_('CTO'),
		'desc':_('Glow是创业奇才Max Levchin在继创立了Paypal，Slide.com之后的又一家公司。以大数据分析，移动计算为核心。'),
		'avatar':'???.jpg',
		'speech':_('《Celery分布式任务队列》'),
	},

    {
	    'fullname':_('袁昕'),
		'nickname':_(' '),
		'company':_('创业中'),
		'position':_('??'),
		'desc':_('他在独自创业后运营自媒体编程教室, 主要推广python语言'),
		'avatar':'???.jpg',
		'speech':_('《编程教室的一些故事》'),
	},
	
    {
	    'fullname':_('赵磊'),
		'nickname':_(' '),
		'company':_('新车间'),
		'position':_('创客'),
		'desc':_('Python的用途多种多样, 你之前有没有听说过 ROS? 机器人的控制系统, 为什么我们不能简单的写一个程序控制步进电机? 为什么在机器人的世界里我们又遇到了框架问题'),
		'avatar':'131129_zhaolei.JPG',
		'speech':_('《Robot Operating System 机器人系统简介》'),
	},

	{
	    'fullname':_('王剑峰'),
		'nickname':_('剑峰王'),
		'company':_('OpenERP'),
		'position':_('社区主要负责人'),
		'desc':_('曾在IBM公司负责ERP相关工作，后来投身开源ERP世界，创立了2家OpenERP的咨询服务公司。'),
		'avatar':'wangjianfeng.jpg',
		'speech':_('CodeLab:介绍Python的企业级应用开源软件OpenERP的快速学习和开发、维护相关技能.'),
	},
    {
        'fullname':_('吕召刚'),
        'nickname':_(''),
        'company':_('大众点评'),
        'position':_('搜索研发经理'),
        'desc':_('长期专注于搜索算法，python爱好者，爱好折腾各种技术'),
        'avatar':'lvshaogang.png',
        'speech':_('《如何在2天内开发一个校园招聘系统-python在大众点评中的应用》'),
    },
    {
        'fullname':_('段华杰'),
        'nickname':_(''),
        'company':_('大众点评'),
        'position':_(''),
        'desc':_('上海交大计算机系硕士毕业，安徽桐城人，2013年4月正式加入大众点评网。在点评网的这段时间，使用django框架开发完成了众包系统、搜索运营系统、开放平台数据管理系统、大众点评面试评估系统。2011年正式学习python，接触后就被python的特性深深折服：简约而不简单。'),
        'avatar':'duanhuajie.png',
        'speech':_('《如何在2天内开发一个校园招聘系统-python在大众点评中的应用》'),
    },
    {
        'fullname':_('曹文炯'),
        'nickname':_(''),
        'company':_('堆糖网'),
        'position':_('技术合伙人'),
        'desc':_('目前为堆糖网技术合伙人，从业12年间，曾任职于阿里巴巴平台架构师，盛大研究员，目前主要致力于人工神经网络，计算机视觉及推荐系统的应用。'),
        'avatar':'caowenjiong.jpg',
        'speech':_('《小清新的文艺复兴 --Python与堆糖的工业化实践》'),
    },

##############################################################################
#
#   杭州  讲师信息
#
##############################################################################


    {
        'fullname':_('屈兴永'),
        'nickname':_('Nimo Qu'),
        'company':_('弘文教育'),
        'position':_('产品经理'),
        'desc':_('08年开始服务于视频娱乐、游戏公司，负责web实时定向数据抓取，实现网页游戏、视频等内容聚合。目前在学习推荐系统、内容挖掘相关知识，欢迎大家交流讨论。'),
        'avatar':'quxingyong.jpg',
        'speech':_('内容聚合与数据抓取'),
    },
    {
        'fullname':_('HepoChen'),
        'nickname':_('HepoChen'),
        'company':_('Z.R.E.Y'),
        'position':_('设计师'),
        'desc':_('我把编码当做设计的一部分，我视设计为哲学的一部分。'),
        'avatar':'HepoChen.jpg',
        'speech':_('《FarBox的Python实践》'),
    },

##############################################################################
#
#   北京  讲师信息
#
##############################################################################
    {
        'fullname':_('李迎辉'),
        'nickname':_('Limodou'),
        'company':_(''),
        'position':_(''),
        'desc':_('Python 中文社区创始人及 Python 技术的关键推广者之一。广受欢迎的 Ulipad 编辑器，以及 web框架 Uliweb 的作者。'),
        'avatar':'liyinghui.jpg',
        'speech':_('《Uliweb比较与实践》'),
    },

    {
	    'fullname':_('程辉'),
		'nickname':_(''),
		'company':_('SINA'),
		'position':_('新浪OpenStack公有云平台(SWS)负责人'),
		'desc':_('新浪云计算技术经理，目前是OpenStack中国社区的管理员，同时也是新浪OpenStack公有云平台(SWS)负责人。2012年8月当选为OpenStack基金会董事会成员。'),
		'avatar':'huicheng.jpg',
		'speech':_('《基于OpenStack建设公有云平台的开发实践》'),
	},

    {
        'fullname':_('卢亿雷'),
        'nickname':_(' '),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《Python在广告监测数据中的分析应用》'),
    },

    {
        'fullname':_('梁瀚'),
        'nickname':_(' '),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《网络射击手游High Noon 2基于Python的服务器架构》'),
    },

    {
        'fullname':_('潘凌涛'),
        'nickname':_(' '),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《介绍 Seafile，开源、专业的私有云存储》'),
    },

    {
        'fullname':_('黄昆'),
        'nickname':_(' '),
        'company':_('???'),
        'position':_('???'),
        'desc':_('???'),
        'avatar':'???.jpg',
        'speech':_('《   python in openstack》(codelab)'),
    },

##############################################################################
#
#   失效  讲师信息
#
##############################################################################
    {
        'fullname':_('沈崴'),
        'nickname':_('沈游侠'),
        'company':_('湖州迅普信息技术有限公司'),
        'position':_('创始人'),
        'desc':_('资深 python 开发者，高效能服务器 eurasia 的作者。湖州迅普信息技术有限公司创始人，广州遛宝计算机技术有限公司联合创始人、技术总监。'),
        'avatar':'shenwai.jpg',
        'speech':_('《Python 产品构建与发布指南》'),
    },


    {
        'fullname':_('殷海明'),
        'nickname':_(''),
        'company':_('一家投资顾问咨询公司'),
        'position':_('技术总监'),
        'desc':_('关注新技术，热爱 Python, Linux，云计算，自动化交易。喜欢美食和美女。'),
        'avatar':'???.png',
        'speech':_('《Pandas实战体验》'),
        'speech_desc':_(' 倾向介绍我的 Datafeed，或 Pandas，或 Python 科学计算生态 :-)'),
    },


    {
        'fullname':_('王捷'),
        'nickname':_(''),
        'company':_('扇贝网'),
        'position':_('扇贝网总经理'),
        'desc':_('王捷，扇贝网总经理，毕业于东南大学和比利时鲁汶大学，曾先后在趋势科技中国研发中心，比利时Attentio，上海CIC担任开发工程师和研发总监等职位。'),
        'avatar':'wangjie.jpg',
        'speech':_('《Python小团队不妨知道的技术》'),
    },


    {
        'fullname':_('林伟'),
        'nickname':_(''),
        'company':_('网易'),
        'position':_('资深技术主管'),
        'desc':_('网易资深技术主管，18年程序设计经验。'),
        'avatar':'linwei.jpg',
        'speech':_('《实战游戏客户端》'),
    },

    {
        'fullname':_('董洵'),
        'nickname':_(' Alex Dong'),
        'company':_(''),
        'position':_(''),
        'desc':_('对角巷创始人, 好看簿创始人之一. 微软2004年评出的全球56个架构师MVP中唯一的中国人. 他对历史和艺术有浓厚的兴趣, 相信结构的力量. 在不工作的时候, 他喜欢品南方绿茶,听各式音乐,看历史/经济/科幻/技术书籍. 曾经是半职业游泳运动员的他更喜欢绕着玉渊潭跑上15公里,出一身汗. 他还喜欢打篮球,中投自认还不赖.'),
        'avatar':'',
        'speech':_('《国外 Py 社区的组织以及技术发展特点》'),
    },

    
]
