##ContigPull_v3.md

##This is an example of running ContigPull_v3.py for pulling contigs that map to family level tax ID 5654 (Trypanosomatidae) for sample CMS001_035. 

##Note 2 key directories, analysis and sequences, need to hold specific files for this to work.
 
##analysis directory contents prior to starting: needs ContigPull_v3.py and contigPull.sh scripts, along with the contig summary file for CMS001_035 you can download from IDseq Report Details tab. 

Kistler-MacBook:analysis amy.kistler$ ls -lFh
total 1040
-rw-r--r--@ 1 amy.kistler  staff   504K Jan 21 12:46 CMS001_035_Ra_S20_contigs_summary.csv
-rw-r--r--@ 1 amy.kistler  staff   6.5K Jan 21 12:45 ContigPull_v3.py
-rwxr-xr-x  1 amy.kistler  staff   514B Jan 21 12:56 contigPull.sh*

##sequences directory contents prior to starting: need to have the CMS001_035 contigs fasta file you can download from IDseq Report Details tab.

Kistler-MacBook:analysis amy.kistler$ ls -lFh ../sequences/
total 4968
-rw-r--r--@ 1 amy.kistler  staff   2.4M Jan 21 12:48 CMS001_035_Ra_S20_contigs.fasta

##in analysis directory, you kick off the program:

Kistler-MacBook:analysis amy.kistler$ python ContigPull_v3.py CMS001_035_Ra_S20_contigs_summary.csv ../sequences/CMS001_035_Ra_S20_contigs.fasta family 5654

##here's the output printed to screen you should see:

Summary of input information you provided:
Contig summary file = CMS001_035_Ra_S20_contigs_summary.csv
Sample = CMS001_035_
tax_level = family
tax_id = 5654
Contig fasta file = CMS001_035_Ra_S20_contigs.fasta

Pandas dataframe created from contig summary file. There are 2675 rows
2196 rows have contigs > 300bp
NR.family_taxid
NT.family_taxid
992 rows have NR matches to 5654 and tax level
250 rows have NT matches to the 5654 and tax level
469 rows from the NR taxID matches show e-value < 1e-2
250 rows from the NT taxID matches show e-value < 1e-2
ContigPull_v3.py:112: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
  dfAll300taxNR1e2E['NR.PercentQueryAligned'] = (dfAll300taxNR1e2E['NR.Alignment Length']*3)/dfAll300taxNR1e2E['contig_length']
396 rows from the NR taxID matches show alignments > 50% query contig length
219 rows from the NT taxID matches show alignments > 50% query contig length

Here is the NR node list
Index(['NODE_984_length_473_cov_0.737374', 'NODE_1058_length_456_cov_0.638522',
       'NODE_1071_length_453_cov_0.760638',
       'NODE_1093_length_449_cov_0.784946',
       'NODE_1148_length_439_cov_0.657459',
       'NODE_1168_length_436_cov_0.788301',
       'NODE_1177_length_435_cov_0.815642',
       'NODE_1179_length_435_cov_0.798883',
       'NODE_1183_length_434_cov_0.781513',
       'NODE_1216_length_428_cov_0.754986',
       ...
       'NODE_17_length_2753_cov_2.347160', 'NODE_26_length_2322_cov_2.734521',
       'NODE_27_length_2297_cov_1.892342',
       'NODE_2055_length_340_cov_40.315589',
       'NODE_1792_length_360_cov_560.692580',
       'NODE_2584_length_302_cov_1.360000',
       'NODE_857_length_502_cov_985.705882',
       'NODE_1011_length_465_cov_1961.170103',
       'NODE_685_length_551_cov_1708.755274',
       'NODE_862_length_501_cov_2413.030660'],
      dtype='object', name='contig_name', length=396)

Here is the NT node list
Index(['NODE_1058_length_456_cov_0.638522',
       'NODE_1093_length_449_cov_0.784946',
       'NODE_1216_length_428_cov_0.754986',
       'NODE_1245_length_422_cov_0.846377',
       'NODE_1292_length_415_cov_0.860947',
       'NODE_1349_length_408_cov_0.879154',
       'NODE_1350_length_408_cov_0.873112',
       'NODE_1418_length_399_cov_0.903727',
       'NODE_1424_length_398_cov_0.859813',
       'NODE_1630_length_375_cov_0.979866',
       ...
       'NODE_2584_length_302_cov_1.360000',
       'NODE_466_length_642_cov_346.054867',
       'NODE_857_length_502_cov_985.705882',
       'NODE_99_length_1180_cov_509.263826',
       'NODE_1011_length_465_cov_1961.170103',
       'NODE_685_length_551_cov_1708.755274',
       'NODE_1235_length_423_cov_2796.589595',
       'NODE_862_length_501_cov_2413.030660',
       'NODE_34_length_2035_cov_708.600102',
       'NODE_8_length_3317_cov_1829.662654'],
      dtype='object', name='contig_name', length=219)

A total of 419 unique NR or NT alignments that met all criteria were found for the taxID
Here are the contig node ids that align to taxID 5654:
['NODE_984_length_473_cov_0.737374', 'NODE_1058_length_456_cov_0.638522', 'NODE_1071_length_453_cov_0.760638', 'NODE_1093_length_449_cov_0.784946', 'NODE_1148_length_439_cov_0.657459', 'NODE_1168_length_436_cov_0.788301', 'NODE_1177_length_435_cov_0.815642', 'NODE_1179_length_435_cov_0.798883', 'NODE_1183_length_434_cov_0.781513', 'NODE_1216_length_428_cov_0.754986', 'NODE_1245_length_422_cov_0.846377', 'NODE_1250_length_421_cov_0.848837', 'NODE_1275_length_418_cov_0.747801', 'NODE_1292_length_415_cov_0.860947', 'NODE_1300_length_414_cov_0.715134', 'NODE_1338_length_409_cov_0.674699', 'NODE_1349_length_408_cov_0.879154', 'NODE_1350_length_408_cov_0.873112', 'NODE_1418_length_399_cov_0.903727', 'NODE_1424_length_398_cov_0.859813', 'NODE_1432_length_397_cov_0.909375', 'NODE_1443_length_396_cov_0.749216', 'NODE_1531_length_385_cov_0.779221', 'NODE_1550_length_383_cov_0.905229', 'NODE_1572_length_380_cov_0.963696', 'NODE_1594_length_378_cov_0.970100', 'NODE_1630_length_375_cov_0.979866', 'NODE_1631_length_375_cov_0.842282', 'NODE_1634_length_375_cov_0.741611', 'NODE_1644_length_374_cov_0.983165', 'NODE_1647_length_374_cov_0.757576', 'NODE_1666_length_371_cov_0.925170', 'NODE_1712_length_366_cov_0.823529', 'NODE_1723_length_365_cov_1.013889', 'NODE_1725_length_365_cov_0.857639', 'NODE_1727_length_365_cov_0.763889', 'NODE_1737_length_364_cov_0.972125', 'NODE_1766_length_362_cov_0.877193', 'NODE_1809_length_359_cov_1.028369', 'NODE_1811_length_359_cov_0.971631', 'NODE_1833_length_358_cov_0.637011', 'NODE_1883_length_353_cov_1.057971', 'NODE_1902_length_352_cov_0.756364', 'NODE_1906_length_352_cov_0.530909', 'NODE_1916_length_351_cov_0.781022', 'NODE_1922_length_350_cov_1.065934', 'NODE_1942_length_348_cov_1.003690', 'NODE_1958_length_347_cov_1.081481', 'NODE_1959_length_347_cov_1.081481', 'NODE_2001_length_344_cov_0.913858', 'NODE_2059_length_340_cov_1.110266', 'NODE_2112_length_335_cov_0.953488', 'NODE_2190_length_329_cov_1.158730', 'NODE_2194_length_329_cov_1.003968', 'NODE_2207_length_328_cov_1.031873', 'NODE_2299_length_321_cov_1.196721', 'NODE_2318_length_320_cov_1.201646', 'NODE_2320_length_320_cov_1.028807', 'NODE_2391_length_315_cov_1.226891', 'NODE_2417_length_313_cov_1.105932', 'NODE_2427_length_313_cov_0.538136', 'NODE_2478_length_309_cov_1.254310', 'NODE_2491_length_308_cov_0.948052', 'NODE_2505_length_307_cov_1.269565', 'NODE_2516_length_306_cov_1.270742', 'NODE_2530_length_305_cov_1.109649', 'NODE_2532_length_305_cov_0.978070', 'NODE_2534_length_305_cov_0.960526', 'NODE_2546_length_305_cov_0.609649', 'NODE_2549_length_304_cov_1.185022', 'NODE_2595_length_301_cov_0.946429', 'NODE_734_length_536_cov_0.795207', 'NODE_780_length_523_cov_0.778027', 'NODE_802_length_517_cov_0.818182', 'NODE_820_length_511_cov_0.735023', 'NODE_868_length_501_cov_0.808962', 'NODE_995_length_471_cov_0.703046', 'NODE_1003_length_468_cov_0.864450', 'NODE_1005_length_467_cov_0.835897', 'NODE_1073_length_453_cov_0.590426', 'NODE_1083_length_450_cov_0.978552', 'NODE_1085_length_450_cov_0.895442', 'NODE_1103_length_447_cov_0.945946', 'NODE_1104_length_447_cov_0.872973', 'NODE_1113_length_446_cov_0.639566', 'NODE_1170_length_436_cov_0.704735', 'NODE_1180_length_435_cov_0.731844', 'NODE_1203_length_430_cov_1.033994', 'NODE_1220_length_427_cov_0.862857', 'NODE_1273_length_418_cov_1.070381', 'NODE_1278_length_417_cov_1.073529', 'NODE_1284_length_416_cov_0.955752', 'NODE_1298_length_414_cov_0.866469', 'NODE_1311_length_412_cov_0.746269', 'NODE_1329_length_410_cov_0.720721', 'NODE_1342_length_408_cov_1.060423', 'NODE_1368_length_406_cov_0.948328', 'NODE_1376_length_405_cov_0.658537', 'NODE_1388_length_403_cov_1.095092', 'NODE_1437_length_396_cov_1.125392', 'NODE_1446_length_395_cov_1.144654', 'NODE_1492_length_389_cov_0.881410', 'NODE_1514_length_387_cov_0.870968', 'NODE_1555_length_382_cov_0.957377', 'NODE_1569_length_380_cov_1.204620', 'NODE_1584_length_379_cov_1.129139', 'NODE_1642_length_374_cov_1.228956', 'NODE_1667_length_371_cov_0.765306', 'NODE_1674_length_370_cov_1.245734', 'NODE_1681_length_370_cov_0.692833', 'NODE_1700_length_367_cov_1.006897', 'NODE_1757_length_362_cov_1.277193', 'NODE_1781_length_361_cov_0.982394', 'NODE_1861_length_355_cov_1.050360', 'NODE_1869_length_354_cov_1.317690', 'NODE_1875_length_354_cov_0.758123', 'NODE_1909_length_351_cov_1.138686', 'NODE_2122_length_334_cov_1.140078', 'NODE_2146_length_332_cov_0.960784', 'NODE_2281_length_322_cov_1.191837', 'NODE_2303_length_321_cov_1.065574', 'NODE_2387_length_315_cov_1.529412', 'NODE_2388_length_315_cov_1.525210', 'NODE_2443_length_312_cov_0.451064', 'NODE_2514_length_306_cov_1.283843', 'NODE_2591_length_301_cov_1.629464', 'NODE_602_length_583_cov_0.729249', 'NODE_673_length_556_cov_0.799582', 'NODE_781_length_523_cov_0.755605', 'NODE_824_length_510_cov_0.741339', 'NODE_841_length_506_cov_0.745921', 'NODE_867_length_501_cov_0.882075', 'NODE_882_length_496_cov_0.821002', 'NODE_904_length_490_cov_1.060533', 'NODE_929_length_485_cov_0.602941', 'NODE_938_length_482_cov_1.081481', 'NODE_939_length_482_cov_0.886420', 'NODE_979_length_474_cov_1.103275', 'NODE_1006_length_467_cov_0.815385', 'NODE_1028_length_462_cov_1.046753', 'NODE_1072_length_453_cov_0.619681', 'NODE_1091_length_449_cov_0.865591', 'NODE_1157_length_437_cov_1.216667', 'NODE_1182_length_434_cov_1.224090', 'NODE_1227_length_425_cov_0.839080', 'NODE_1385_length_403_cov_1.343558', 'NODE_1484_length_390_cov_0.837061', 'NODE_1562_length_381_cov_1.440789', 'NODE_1738_length_364_cov_0.891986', 'NODE_1756_length_362_cov_1.392982', 'NODE_1790_length_361_cov_0.704225', 'NODE_1835_length_358_cov_0.576512', 'NODE_2000_length_344_cov_1.022472', 'NODE_2041_length_341_cov_1.401515', 'NODE_2086_length_337_cov_1.580769', 'NODE_2181_length_330_cov_0.928854', 'NODE_2189_length_329_cov_1.234127', 'NODE_2203_length_328_cov_1.422311', 'NODE_2445_length_311_cov_1.598291', 'NODE_2528_length_305_cov_1.916667', 'NODE_2581_length_302_cov_1.653333', 'NODE_568_length_596_cov_0.791908', 'NODE_622_length_576_cov_0.697395', 'NODE_643_length_567_cov_0.959184', 'NODE_677_length_555_cov_0.684100', 'NODE_771_length_525_cov_0.919643', 'NODE_800_length_518_cov_1.058957', 'NODE_884_length_496_cov_0.804296', 'NODE_914_length_488_cov_1.199513', 'NODE_950_length_480_cov_1.044665', 'NODE_975_length_475_cov_1.238693', 'NODE_997_length_470_cov_1.180662', 'NODE_999_length_469_cov_0.931122', 'NODE_1027_length_462_cov_1.244156', 'NODE_1068_length_453_cov_1.265957', 'NODE_1078_length_451_cov_1.021390', 'NODE_1153_length_438_cov_0.961219', 'NODE_1164_length_436_cov_1.169916', 'NODE_1213_length_428_cov_1.227920', 'NODE_1358_length_407_cov_1.106061', 'NODE_1457_length_394_cov_1.605678', 'NODE_1507_length_387_cov_1.416129', 'NODE_1626_length_375_cov_1.674497', 'NODE_1641_length_374_cov_1.242424', 'NODE_1683_length_369_cov_1.695205', 'NODE_1931_length_349_cov_1.797794', 'NODE_2024_length_342_cov_1.347170', 'NODE_2087_length_337_cov_1.492308', 'NODE_2089_length_337_cov_1.000000', 'NODE_2585_length_302_cov_1.288889', 'NODE_339_length_731_cov_0.785933', 'NODE_420_length_670_cov_0.984823', 'NODE_434_length_662_cov_0.781197', 'NODE_451_length_651_cov_0.763066', 'NODE_474_length_639_cov_0.882562', 'NODE_541_length_609_cov_1.001880', 'NODE_575_length_593_cov_0.990310', 'NODE_584_length_589_cov_1.140625', 'NODE_666_length_558_cov_0.754678', 'NODE_683_length_552_cov_0.705263', 'NODE_730_length_536_cov_1.228758', 'NODE_778_length_523_cov_0.926009', 'NODE_834_length_507_cov_1.304651', 'NODE_937_length_482_cov_1.135802', 'NODE_943_length_481_cov_1.443069', 'NODE_1109_length_446_cov_1.569106', 'NODE_1112_length_446_cov_0.929539', 'NODE_1163_length_436_cov_1.334262', 'NODE_1333_length_409_cov_1.099398', 'NODE_1384_length_403_cov_1.539877', 'NODE_1846_length_356_cov_1.344086', 'NODE_1917_length_350_cov_1.948718', 'NODE_1918_length_350_cov_1.395604', 'NODE_1941_length_348_cov_1.579336', 'NODE_2221_length_327_cov_1.272000', 'NODE_563_length_599_cov_1.011494', 'NODE_617_length_577_cov_0.780000', 'NODE_667_length_557_cov_1.368750', 'NODE_670_length_556_cov_1.200418', 'NODE_720_length_540_cov_0.866091', 'NODE_799_length_518_cov_1.319728', 'NODE_823_length_510_cov_1.200924', 'NODE_852_length_503_cov_1.223005', 'NODE_872_length_500_cov_1.515366', 'NODE_891_length_493_cov_1.033654', 'NODE_1208_length_429_cov_1.136364', 'NODE_1212_length_428_cov_1.256410', 'NODE_1639_length_374_cov_2.212121', 'NODE_2103_length_336_cov_1.019305', 'NODE_2206_length_328_cov_1.095618', 'NODE_284_length_802_cov_1.147586', 'NODE_422_length_668_cov_1.199662', 'NODE_435_length_660_cov_0.907376', 'NODE_459_length_646_cov_1.073814', 'NODE_528_length_616_cov_0.957328', 'NODE_542_length_608_cov_1.107345', 'NODE_654_length_561_cov_1.150826', 'NODE_753_length_529_cov_1.064159', 'NODE_974_length_475_cov_1.650754', 'NODE_1061_length_455_cov_1.645503', 'NODE_1318_length_411_cov_1.476048', 'NODE_1534_length_384_cov_1.100977', 'NODE_1624_length_375_cov_2.312081', 'NODE_1649_length_373_cov_1.462838', 'NODE_223_length_862_cov_0.979618', 'NODE_606_length_581_cov_1.117063', 'NODE_607_length_580_cov_1.121272', 'NODE_609_length_579_cov_1.290837', 'NODE_708_length_544_cov_1.406852', 'NODE_768_length_525_cov_1.517857', 'NODE_1012_length_465_cov_1.628866', 'NODE_1107_length_447_cov_0.627027', 'NODE_1688_length_368_cov_1.914089', 'NODE_294_length_788_cov_1.021097', 'NODE_312_length_763_cov_0.969388', 'NODE_470_length_642_cov_0.900885', 'NODE_572_length_594_cov_1.686654', 'NODE_573_length_594_cov_1.032882', 'NODE_696_length_548_cov_1.543524', 'NODE_1640_length_374_cov_1.646465', 'NODE_281_length_804_cov_1.302613', 'NODE_370_length_702_cov_1.478400', 'NODE_530_length_615_cov_1.356877', 'NODE_712_length_543_cov_1.394850', 'NODE_814_length_513_cov_1.006881', 'NODE_844_length_505_cov_1.588785', 'NODE_1272_length_418_cov_2.445748', 'NODE_1367_length_406_cov_1.200608', 'NODE_104_length_1165_cov_0.958640', 'NODE_116_length_1100_cov_0.909091', 'NODE_235_length_847_cov_1.125974', 'NODE_279_length_806_cov_1.345679', 'NODE_290_length_795_cov_1.000000', 'NODE_378_length_694_cov_1.371151', 'NODE_439_length_658_cov_1.043029', 'NODE_648_length_563_cov_1.362140', 'NODE_931_length_484_cov_1.619165', 'NODE_1026_length_462_cov_2.335065', 'NODE_2011_length_343_cov_2.477444', 'NODE_333_length_735_cov_0.898176', 'NODE_344_length_726_cov_1.338983', 'NODE_386_length_687_cov_1.334426', 'NODE_562_length_599_cov_1.398467', 'NODE_1377_length_404_cov_3.639144', 'NODE_1939_length_348_cov_3.863469', 'NODE_301_length_775_cov_0.997135', 'NODE_330_length_736_cov_1.646434', 'NODE_492_length_628_cov_1.929220', 'NODE_2010_length_343_cov_3.609023', 'NODE_214_length_880_cov_1.372354', 'NODE_798_length_518_cov_2.183673', 'NODE_1173_length_435_cov_2.167598', 'NODE_2098_length_336_cov_1.749035', 'NODE_2401_length_314_cov_4.063291', 'NODE_107_length_1127_cov_0.840952', 'NODE_204_length_901_cov_0.850728', 'NODE_253_length_831_cov_1.494695', 'NODE_560_length_599_cov_2.086207', 'NODE_805_length_516_cov_1.744875', 'NODE_1040_length_459_cov_2.476440', 'NODE_1487_length_389_cov_3.125000', 'NODE_458_length_646_cov_2.198594', 'NODE_115_length_1111_cov_1.272727', 'NODE_183_length_944_cov_1.659746', 'NODE_193_length_927_cov_1.375294', 'NODE_264_length_819_cov_1.257412', 'NODE_804_length_516_cov_2.350797', 'NODE_126_length_1073_cov_1.333333', 'NODE_145_length_1023_cov_1.168076', 'NODE_524_length_616_cov_2.649351', 'NODE_536_length_612_cov_1.865421', 'NODE_191_length_930_cov_1.531067', 'NODE_295_length_786_cov_1.724965', 'NODE_109_length_1123_cov_1.336520', 'NODE_385_length_688_cov_2.584288', 'NODE_656_length_560_cov_2.730849', 'NODE_237_length_845_cov_1.872396', 'NODE_310_length_765_cov_2.257267', 'NODE_479_length_636_cov_2.422182', 'NODE_87_length_1245_cov_1.256849', 'NODE_153_length_1007_cov_1.767742', 'NODE_408_length_676_cov_1.520868', 'NODE_585_length_588_cov_2.962818', 'NODE_651_length_562_cov_2.777320', 'NODE_788_length_521_cov_3.403153', 'NODE_885_length_495_cov_3.918660', 'NODE_245_length_838_cov_2.082786', 'NODE_298_length_777_cov_2.500000', 'NODE_166_length_978_cov_1.791343', 'NODE_288_length_795_cov_2.569638', 'NODE_556_length_602_cov_2.676190', 'NODE_74_length_1351_cov_1.549451', 'NODE_165_length_979_cov_2.054324', 'NODE_311_length_763_cov_2.599125', 'NODE_432_length_662_cov_3.174359', 'NODE_695_length_548_cov_3.796178', 'NODE_80_length_1288_cov_1.237820', 'NODE_360_length_709_cov_3.689873', 'NODE_534_length_613_cov_4.061567', 'NODE_783_length_522_cov_3.741573', 'NODE_287_length_796_cov_2.751043', 'NODE_401_length_679_cov_3.098007', 'NODE_619_length_576_cov_3.633267', 'NODE_67_length_1457_cov_1.621739', 'NODE_252_length_831_cov_3.009284', 'NODE_577_length_592_cov_3.988350', 'NODE_674_length_555_cov_3.784519', 'NODE_78_length_1310_cov_1.708840', 'NODE_325_length_741_cov_3.100904', 'NODE_489_length_630_cov_3.714286', 'NODE_146_length_1021_cov_1.612288', 'NODE_186_length_936_cov_2.619325', 'NODE_212_length_885_cov_3.116337', 'NODE_419_length_670_cov_3.784148', 'NODE_93_length_1203_cov_2.267318', 'NODE_187_length_934_cov_3.236873', 'NODE_69_length_1450_cov_1.566642', 'NODE_167_length_977_cov_2.418889', 'NODE_455_length_647_cov_3.875439', 'NODE_491_length_629_cov_4.554348', 'NODE_119_length_1090_cov_2.855874', 'NODE_593_length_585_cov_5.653543', 'NODE_395_length_683_cov_4.764026', 'NODE_108_length_1124_cov_2.428844', 'NODE_316_length_755_cov_4.351032', 'NODE_433_length_662_cov_2.945299', 'NODE_217_length_872_cov_3.412579', 'NODE_144_length_1023_cov_2.086681', 'NODE_83_length_1268_cov_2.375315', 'NODE_260_length_823_cov_3.981233', 'NODE_277_length_807_cov_3.942466', 'NODE_147_length_1019_cov_3.429936', 'NODE_400_length_679_cov_6.289037', 'NODE_101_length_1173_cov_3.204380', 'NODE_54_length_1632_cov_2.322830', 'NODE_177_length_954_cov_4.727480', 'NODE_23_length_2372_cov_1.643137', 'NODE_66_length_1471_cov_2.573171', 'NODE_130_length_1063_cov_3.051724', 'NODE_38_length_1934_cov_2.399031', 'NODE_68_length_1454_cov_3.039942', 'NODE_158_length_1001_cov_4.049784', 'NODE_19_length_2617_cov_2.168898', 'NODE_117_length_1099_cov_3.866928', 'NODE_33_length_2048_cov_2.948250', 'NODE_30_length_2107_cov_2.472414', 'NODE_17_length_2753_cov_2.347160', 'NODE_26_length_2322_cov_2.734521', 'NODE_27_length_2297_cov_1.892342', 'NODE_2055_length_340_cov_40.315589', 'NODE_1792_length_360_cov_560.692580', 'NODE_2584_length_302_cov_1.360000', 'NODE_857_length_502_cov_985.705882', 'NODE_1011_length_465_cov_1961.170103', 'NODE_685_length_551_cov_1708.755274', 'NODE_862_length_501_cov_2413.030660', 'NODE_2251_length_325_cov_0.794355', 'NODE_517_length_618_cov_0.890943', 'NODE_278_length_807_cov_1.590411', 'NODE_477_length_637_cov_2.014286', 'NODE_225_length_859_cov_2.196931', 'NODE_273_length_811_cov_3.006812', 'NODE_2573_length_303_cov_0.756637', 'NODE_283_length_802_cov_4.240000', 'NODE_36_length_1994_cov_1.617110', 'NODE_334_length_734_cov_5.302892', 'NODE_583_length_589_cov_6.613281', 'NODE_1476_length_390_cov_32.910543', 'NODE_1125_length_443_cov_118.942623', 'NODE_2444_length_311_cov_183.658120', 'NODE_1734_length_364_cov_320.714286', 'NODE_1435_length_396_cov_300.821317', 'NODE_2244_length_325_cov_513.229839', 'NODE_2039_length_341_cov_434.212121', 'NODE_466_length_642_cov_346.054867', 'NODE_99_length_1180_cov_509.263826', 'NODE_1235_length_423_cov_2796.589595', 'NODE_34_length_2035_cov_708.600102', 'NODE_8_length_3317_cov_1829.662654']

Node list has been written to CMS001_035_Ra_S20_family_5654_ContigNodeHits.txt

Now using node list to pull contig records from CMS001_035_Ra_S20_contigs.fasta
Done! Contigs should be found in ../sequences/CMS001_035_Ra_S20_family_5654_ContigNodeHits.fasta

#Here are output files generated and saved to analysis directory

Kistler-MacBook:analysis amy.kistler$ ls -lFh
total 1080
-rw-r--r--@ 1 amy.kistler  staff   504K Jan 21 12:46 CMS001_035_Ra_S20_contigs_summary.csv
-rw-r--r--  1 amy.kistler  staff    14K Jan 21 12:58 CMS001_035_Ra_S20_family_5654_ContigNodeHits.txt
-rw-r--r--@ 1 amy.kistler  staff   6.5K Jan 21 12:45 ContigPull_v3.py
-rwxr-xr-x  1 amy.kistler  staff   262B Jan 21 12:57 contigPull.sh*
-rw-r--r--  1 amy.kistler  staff    58B Jan 21 12:58 sample_listFile

#Here are output files generated and saved to sequences directory

Kistler-MacBook:analysis amy.kistler$ cd ../sequences/
Kistler-MacBook:sequences amy.kistler$ ls -lFh
total 5496
-rw-r--r--@ 1 amy.kistler  staff   2.4M Jan 21 12:48 CMS001_035_Ra_S20_contigs.fasta
-rw-r--r--  1 amy.kistler  staff   261K Jan 21 12:58 CMS001_035_Ra_S20_family_5654_ContigNodeHits.fasta
