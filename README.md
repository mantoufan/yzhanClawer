# YZhanClawer

Clawing website to transform page to structured data.

## Support List

- Boss 直聘：https://www.zhipin.com

## Instructions

### 1. Install Chinese fonts

To ensure proper display of Chinese characters, install the required Chinese fonts:

```bash
sudo apt-get install ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming
```

### 2. Install the browser

To run the scraper, install the Chrome browser and set it up.  
Please run it in the project directory:

```bash
sudo apt-get install unzip
unzip https://drfs.ctcontents.com/file/3312/1381784230/e140ca/github/chrome-linux64-114.0.5735.90.zip -d ~/
mv ~/chrome-linux64 ~/chrome
ln -s ~/chrome/chrome /usr/local/bin/chrome
chmod +x ~/chrome
```

### 3. Install dependencies

Before running the scraper, ensure that all the necessary Python dependencies are installed.  
Please run it in the project directory:

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

Once everything is installed, you can start the scraper using.  
Please run it in the project directory:

```bash
python main.py
```

- **Step 1:** A Chrome browser will open automatically.
- **Step 2:** Optional, you will have **30 seconds** to scan the QR code and log in to the website.
- **Step 3:** Wait for the scraper to finish.

### 5. Configuration File (`config.py`)

Each website's configuration file: `crawlers/{website name}/config.py`

#### BOSS 直聘

Here’s an example configuration file to specify the jobs, cities, and other filters you want to scrape:

```python
# Specify the job positions, cities, and filters to scrape.
# Comment out any unnecessary lines with a '#' at the beginning.

jobs = [  # List of jobs to search for
    'Java',  # 100101
    "C-C++",  # 100102
    'PHP',  # 100103
    # 'Python',  # 100109
    # "C#",  # 100106
    # 'Golang',  # 100116
    # 'JavaScript',
    # 'Swift',
    # 'Ruby',
    # 'Kotlin'
]

experience = ",".join([  # Work experience filters, comment out the ones you don't need
    # '108',  # Current student
    # '102',  # Fresh graduate
    # '101',  # No experience required
    # '103',  # Less than 1 year
    # '104',  # 1-3 years
    # '105',  # 3-5 years
    # '106',  # 5-10 years
    # '107',  # Over 10 years
])

degree = ",".join([  # Education requirements
    # '209',  # Junior high or below
    # '208',  # Technical secondary school
    # '206',  # High school
    # '202',  # Associate's degree
    # '203',  # Bachelor's degree
    # '204',  # Master's degree
    # '205',  # Doctorate
])

citys = {  # Cities to search in, comment out any cities you don't want
  101070300: '鞍山',
  101110700: '安康',
  101180200: '安阳',
  101220600: '安庆',
  101260300: '安顺',
  101330100: '澳门',
  101271900: '阿坝藏族羌族自治州',
  101081200: '阿拉善盟',
  101140700: '阿里地区',
  101131000: '阿克苏地区',
  101131500: '阿勒泰地区',
  101131700: '阿拉尔',
  101010100: '北京',
  101060500: '白城',
  101060800: '白山',
  101070500: '本溪',
  101080200: '包头',
  101080800: '巴彦淖尔',
  101090200: '保定',
  101110900: '宝鸡',
  101121100: '滨州',
  101161000: '白银',
  101220200: '蚌埠',
  101220900: '亳州',
  101260500: '毕节',
  101270900: '巴中',
  101290300: '保山',
  101301000: '百色',
  101301300: '北海',
  101130400: '巴音郭楞蒙古自治州',
  101130500: '博尔塔拉蒙古自治州',
  101311400: '白沙黎族自治县',
  101311800: '保亭黎族苗族自治县',
  101132100: '北屯市',
  101040100: '重庆',
  101060100: '长春',
  101071200: '朝阳',
  101080500: '赤峰',
  101090400: '承德',
  101090700: '沧州',
  101100500: '长治',
  101191100: '常州',
  101221000: '滁州',
  101221500: '池州',
  101250100: '长沙',
  101250500: '郴州',
  101250600: '常德',
  101270100: '成都',
  101281500: '潮州',
  101300200: '崇左',
  101291700: '楚雄彝族自治州',
  101130300: '昌吉回族自治州',
  101311200: '澄迈',
  101311500: '昌江黎族自治县',
  101140300: '昌都',
  101050800: '大庆',
  101070200: '大连',
  101070600: '丹东',
  101100200: '大同',
  101120400: '德州',
  101121200: '东营',
  101160200: '定西',
  101270600: '达州',
  101271700: '德阳',
  101281600: '东莞',
  101291300: '德宏傣族景颇族自治州',
  101291500: '迪庆藏族自治州',
  101291600: '大理白族自治州',
  101051300: '大兴安岭地区',
  101310400: '儋州',
  101310900: '东方',
  101311000: '定安',
  101282200: '东沙群岛',
  101080600: '鄂尔多斯',
  101200300: '鄂州',
  101201300: '恩施土家族苗族自治州',
  101070400: '抚顺',
  101070900: '阜新',
  101220800: '阜阳',
  101230100: '福州',
  101240400: '抚州',
  101280800: '佛山',
  101301400: '防城港',
  101170400: '固原',
  101240700: '赣州',
  101260100: '贵阳',
  101270800: '广安',
  101271800: '广元',
  101280100: '广州',
  101300500: '桂林',
  101300800: '贵港',
  101272100: '甘孜藏族自治州',
  101161400: '甘南藏族自治州',
  101150600: '果洛藏族自治州',
  101050100: '哈尔滨',
  101050600: '黑河',
  101051100: '鹤岗',
  101071400: '葫芦岛',
  101080100: '呼和浩特',
  101080700: '呼伦贝尔',
  101090800: '衡水',
  101091000: '邯郸',
  101110800: '汉中',
  101121000: '菏泽',
  101150200: '海东',
  101181200: '鹤壁',
  101190900: '淮安',
  101200500: '黄冈',
  101200600: '黄石',
  101210100: '杭州',
  101210200: '湖州',
  101220100: '合肥',
  101220400: '淮南',
  101221100: '淮北',
  101221600: '黄山',
  101250400: '衡阳',
  101251200: '怀化',
  101280300: '惠州',
  101281200: '河源',
  101300700: '贺州',
  101301200: '河池',
  101310100: '海口',
  101291200: '红河哈尼族彝族自治州',
  101150300: '海北藏族自治州',
  101150400: '黄南藏族自治州',
  101150500: '海南藏族自治州',
  101150800: '海西蒙古族藏族自治州',
  101130900: '哈密',
  101131300: '和田地区',
  101050400: '佳木斯',
  101051000: '鸡西',
  101060200: '吉林',
  101070700: '锦州',
  101100400: '晋中',
  101100600: '晋城',
  101120100: '济南',
  101120700: '济宁',
  101160600: '金昌',
  101160800: '酒泉',
  101161200: '嘉峪关',
  101181100: '焦作',
  101200800: '荆州',
  101201200: '荆门',
  101210300: '嘉兴',
  101210900: '金华',
  101240200: '九江',
  101240600: '吉安',
  101240800: '景德镇',
  101281100: '江门',
  101281900: '揭阳',
  101181800: '济源',
  101130200: '克拉玛依',
  101180800: '开封',
  101290100: '昆明',
  101131100: '克孜勒苏柯尔克孜自治州',
  101131200: '喀什地区',
  101132200: '可克达拉市',
  101132300: '昆玉市',
  101060600: '辽源',
  101071000: '辽阳',
  101090600: '廊坊',
  101100700: '临汾',
  101101100: '吕梁',
  101120900: '临沂',
  101121700: '聊城',
  101140100: '拉萨',
  101160100: '兰州',
  101161100: '陇南',
  101180900: '洛阳',
  101181500: '漯河',
  101191000: '连云港',
  101210800: '丽水',
  101221400: '六安',
  101230700: '龙岩',
  101250800: '娄底',
  101260600: '六盘水',
  101271000: '泸州',
  101271400: '乐山',
  101290800: '临沧',
  101290900: '丽江',
  101300300: '柳州',
  101300400: '来宾',
  101272000: '凉山彝族自治州',
  101161300: '临夏回族自治州',
  101311300: '临高',
  101311600: '乐东黎族自治县',
  101311700: '陵水黎族自治县',
  101140400: '林芝',
  101050300: '牡丹江',
  101220500: '马鞍山',
  101270400: '绵阳',
  101271500: '眉山',
  101280400: '梅州',
  101282000: '茂名',
  101180700: '南阳',
  101190100: '南京',
  101190500: '南通',
  101210400: '宁波',
  101230300: '宁德',
  101230900: '南平',
  101240100: '南昌',
  101270500: '南充',
  101271200: '内江',
  101300100: '南宁',
  101291400: '怒江傈僳族自治州',
  101140600: '那曲',
  101071300: '盘锦',
  101160300: '平凉',
  101180500: '平顶山',
  101181300: '濮阳',
  101230400: '莆田',
  101240900: '萍乡',
  101270200: '攀枝花',
  101290500: '普洱',
  101050200: '齐齐哈尔',
  101050900: '七台河',
  101091100: '秦皇岛',
  101120200: '青岛',
  101160400: '庆阳',
  101211000: '衢州',
  101230500: '泉州',
  101281300: '清远',
  101290200: '曲靖',
  101301100: '钦州',
  101260700: '黔东南苗族侗族自治州',
  101260800: '黔南布依族苗族自治州',
  101260900: '黔西南布依族苗族自治州',
  101201500: '潜江',
  101310600: '琼海',
  101311900: '琼中黎族苗族自治县',
  101121500: '日照',
  101140200: '日喀则',
  101020100: '上海',
  101050500: '绥化',
  101051200: '双鸭山',
  101060300: '四平',
  101060700: '松原',
  101070100: '沈阳',
  101090100: '石家庄',
  101100900: '朔州',
  101110600: '商洛',
  101170200: '石嘴山',
  101181000: '商丘',
  101181700: '三门峡',
  101190400: '苏州',
  101191300: '宿迁',
  101201000: '十堰',
  101201100: '随州',
  101210500: '绍兴',
  101220700: '宿州',
  101230800: '三明',
  101240300: '上饶',
  101250900: '邵阳',
  101270700: '遂宁',
  101280200: '韶关',
  101280500: '汕头',
  101280600: '深圳',
  101282100: '汕尾',
  101310200: '三亚',
  101310300: '三沙',
  101201700: '神农架',
  101140500: '山南',
  101131600: '石河子',
  101132400: '双河市',
  101030100: '天津',
  101060400: '通化',
  101071100: '铁岭',
  101080400: '通辽',
  101090500: '唐山',
  101100100: '太原',
  101111000: '铜川',
  101120800: '泰安',
  101160900: '天水',
  101191200: '泰州',
  101210600: '台州',
  101221200: '铜陵',
  101260400: '铜仁',
  101201600: '天门',
  101311100: '屯昌',
  101130800: '吐鲁番',
  101131400: '塔城地区',
  101131800: '图木舒克',
  101132000: '铁门关',
  101341100: '台湾',
  101080300: '乌海',
  101080900: '乌兰察布',
  101110500: '渭南',
  101120600: '潍坊',
  101121300: '威海',
  101130100: '乌鲁木齐',
  101160500: '武威',
  101170300: '吴忠',
  101190200: '无锡',
  101200100: '武汉',
  101210700: '温州',
  101220300: '芜湖',
  101300600: '梧州',
  101291100: '文山壮族苗族自治州',
  101310500: '五指山',
  101310700: '文昌',
  101310800: '万宁',
  101131900: '五家渠',
  101090900: '邢台',
  101101000: '忻州',
  101110100: '西安',
  101110200: '咸阳',
  101150100: '西宁',
  101180300: '新乡',
  101180400: '许昌',
  101180600: '信阳',
  101190800: '徐州',
  101200200: '襄阳',
  101200400: '孝感',
  101200700: '咸宁',
  101221300: '宣城',
  101230200: '厦门',
  101241000: '新余',
  101250200: '湘潭',
  101320300: '香港',
  101251400: '湘西土家族苗族自治州',
  101291000: '西双版纳傣族自治州',
  101201400: '仙桃',
  101081000: '锡林郭勒盟',
  101081100: '兴安盟',
  101050700: '伊春',
  101070800: '营口',
  101100300: '阳泉',
  101100800: '运城',
  101110300: '延安',
  101110400: '榆林',
  101120500: '烟台',
  101170100: '银川',
  101190600: '扬州',
  101190700: '盐城',
  101200900: '宜昌',
  101240500: '宜春',
  101241100: '鹰潭',
  101250700: '益阳',
  101251000: '岳阳',
  101251300: '永州',
  101271100: '宜宾',
  101271600: '雅安',
  101281400: '云浮',
  101281800: '阳江',
  101290400: '玉溪',
  101300900: '玉林',
  101060900: '延边朝鲜族自治州',
  101150700: '玉树藏族自治州',
  101130600: '伊犁哈萨克自治州',
  101090300: '张家口',
  101120300: '淄博',
  101121400: '枣庄',
  101160700: '张掖',
  101170500: '中卫',
  101180100: '郑州',
  101181400: '周口',
  101181600: '驻马店',
  101190300: '镇江',
  101211100: '舟山',
  101230600: '漳州',
  101250300: '株洲',
  101251100: '张家界',
  101260200: '遵义',
  101270300: '自贡',
  101271300: '资阳',
  101280700: '珠海',
  101280900: '肇庆',
  101281000: '湛江',
  101281700: '中山',
  101290700: '昭通',
}
```

In this configuration file, you can modify:

- **Jobs**: Specify the positions you want to scrape (e.g., Java, C++, PHP, etc.).
- **Experience**: Filter by years of work experience.
- **Degree**: Specify educational qualifications required.
- **Cities**: Define the cities to target (e.g., Shenzhen, Hangzhou, Beijing, etc.).
