from enum import IntEnum, unique


@unique
class ScannerModels(IntEnum):
    BUIC1000 = 2
    BUIC1500 = 3
    TS400 = 400
    CX30 = 30
    CX35 = 35
    TS200 = 200
    TS205 = 205
    TS215 = 215
    TS220 = 220
    TS230 = 230
    TS240 = 240
    TS300 = 300
    TS300EBS = 314
    TS440 = 440
    SB500 = 500
    SB600 = 600
    SB650M = 651
    BX7200 = 7200
    TS240SF = 250
    TS500 = 501
    TSX40 = 40
    TS250 = 10250


@unique
class SmartSourceModels(IntEnum):
    EXPERT_ELITE = 10251
    PRO_ELITE = 10252
    EXPERT_MICRO_ELITE = 10253
    MICRO_ELITE = 10254
    CX35_RNDIS = 1035


@unique
class EjectControl(IntEnum):
    EJECT_TO_DEFAULT = 0
    EJECT_TO_AUX = 1


@unique
class ScanOptions(IntEnum):
    BUIC_SCAN_FRONT = 1
    BUIC_SCAN_BACK = 2
    BUIC_SCAN_BOTH = 3
    BUIC_SCAN_MICR = 4
    BUIC_SCAN_FRONT_MICR = 5
    BUIC_SCAN_BACK_MICR = 6
    BUIC_SCAN_BOTH_MICR = 7


@unique
class ConfigPaths(IntEnum):
    CFG_INIPATH = 135
    CFG_CFGPATH = 136
    CFG_DLLPATH = 137
    CFG_FIRMWAREPATH = 138
    CFG_FONTPATH = 113


class ScannerSettings(IntEnum):
    CFG_SCANNERTYPE = 158
    CFG_MISC_SCANBATCH_ENABLE = 160
    CFG_MISC_FEED_SOLENOID = 161
    CFG_MISC_PRINT_CARTRIDGE = 164
    CFG_MISC_SCAN_MODE = 191
    CFG_MISC_USB1 = 168
    CFG_MISC_VIRTUAL = 170
    CFG_MISC_LATE_JAM_TEST = 185
    CFG_MISC_MICR_VERIFY = 116
    CFG_MISC_MICR_LOWCONFIDENCE = 157
    CFG_MISC_ENABLE_SCAN = 111


class ScannerModes(IntEnum):
    CFG_SCAN_MODE_FORWARD = 0
    CFG_SCAN_MODE_REVERSE = 1
    CFG_SCAN_MODE_HOLD = 2
    CFG_SCAN_MODE_KIOSK = 3
    CFG_SCAN_MODE_DOCUMENT = 4
    CFG_SCAN_MODE_DEPOSIT = 5


class ImageSettings(IntEnum):
    CFG_IMAGE_FORMAT = 92
    CFG_IMAGE_BW = 23
    CFG_IMAGE_GRAY256LEVEL = 45
    CFG_IMAGE_RESOLUTION = 6
    CFG_IMAGE_FRONTONLY = 42
    CFG_IMAGE_FRONTBACK = 43
    CFG_IMAGECROPPING_ENABLE = 36
    CFG_IMAGE_GRAY256LEVEL_16 = 0
    CFG_IMAGE_GRAY256LEVEL_256 = 1
    CFG_IMAGE_BW_BW = 0
    CFG_IMAGE_BW_GRAY = 1


class MICRSettings(IntEnum):
    CFG_MICR_ENABLE = 1
    CFG_MICR_FONT = 2
    CFG_MICR_CMC7 = 0
    CFG_MICR_E13B = 1
    CFG_MICR_AUTO = 2
    CFG_MICR_INITIAL_POS = 14
    CFG_MICR_END_POS = 71


class AuxReaderSettings(IntEnum):
    CFG_AUXREADER_TYPE = 72
    CFG_AUXREADER_FONT = 73
    CFG_AUXREADER_INITIALPOS = 74
    CFG_AUXREADER_ENDPOS = 75
    CFG_AUXREADER_BAUDRATE = 76
    CFG_AUXREADER_PARITY = 77
    CFG_AUXREADER_CHARLENGTH = 78
    CFG_AUXREADER_STOPBIT = 79


class SorterSettings(IntEnum):
    CFG_SORTER_INPUT = 49
    CFG_SORTER_ALGORITHM = 39
    CFG_SORTER_ALG_NONE = 0
    CFG_SORTER_ALG_PRESENT = 1
    CFG_SORTER_ALG_EQUAL = 2
    CFG_SORTER_ALG_NOT_EQUAL = 3
    CFG_SORTER_ALG_GT_EQUAL = 4
    CFG_SORTER_ALG_LT_EQUAL = 5
    CFG_SORTER_ALG_BETWEEN = 6
    CFG_SORTER_ALG_OUTSIDE = 7
    CFG_SORTER_ALG_EQUAL1OR2 = 8
    CFG_SORTER_ALG_NOTEQU1OR2 = 9
    CFG_SORTER_STRING1 = 40
    CFG_SORTER_STRING2 = 41


class PrinterSettings(IntEnum):
    CFG_DEV_PRINTER = 31
    CFG_IJPRINTER_PRINTBMP = 33
    CFG_IJPRINTER_BMPFILENAME = 35
    CFG_IJPRINTER_FONTFILENAME = 83
    CFG_IJPRINTER_INTENSITY = 86
    CFG_IJPRINTER_XPIXELD = 87
    CFG_IJPRINTER_CLEAN44 = 88
    CFG_IJPRINTER_CLEAN18 = 89
    CFG_IJPRINTER_CLEAN6 = 90
    CFG_IJPRINTER_CLEAN2 = 91
    CFG_IJPRINTER_PRINTSTRING = 34


class ImageFormats(IntEnum):
    FORMAT_TIFF_UNCOMP = 0
    FORMAT_TIFF = 1
    FORMAT_TIFF_REVERSE = 9
    FORMAT_BMP = 3
    FORMAT_JPEGG = 4


class DPISettings(IntEnum):
    CFG_IMAGE_RESOL_100X100 = 0
    CFG_IMAGE_RESOL_200X100 = 3
    CFG_IMAGE_RESOL_200X200 = 1
    CFG_IMAGE_RESOL_200X100RAW = 2
    CFG_IMAGE_RESOL_300X300 = 4
    CFG_IMAGE_RESOL_600X600 = 5
    BUIC_DPI100 = 0
    BUIC_DPI200 = 1
    BUIC_DPI200X100 = 3


class MiscSettings(IntEnum):
    CFG_DEV_DOUBLE_FEED = 7
    CFG_MISC_MANUALFEED = 51
    CFG_MICR_GAIN = 193
    CFG_MICR_AGC = 194
    CFG_IMAGE_FRONT_BW_THRESH = 11
    CFG_IMAGE_BACK_BW_THRESH = 12
    CFG_FRANK_MODE_OFF = 0
    CFG_FRANK_MODE_ON = 1
    CFG_FRANK_MODE_MICR = 2
    CFG_FRANK_MODE_EXTERNAL = 3
    CFG_DCCSCAN_MAXTIFFIMAGESIZE = 155
    CFG_DCCSCAN_OPTIONS = 156
    CFG_MISC_PH_ENABLE = 145
    CFG_MISC_TS230_65 = 163
    CFG_MISC_DEBUG_MESSAGES = 162
    CFG_MISC_LOG_MESSAGES = 166
    CFG_REMOTE_MONITOR_LOG = 186
    CFG_REMOTE_MONITOR_LOG_SIZE = 188


class BooleanValues(IntEnum):
    TRUE = 1
    FALSE = 0
    BUIC_DEV_OFF = 0
    BUIC_DEV_ON = 1
    CFG_DEV_OFF = 0
    CFG_DEV_ON = 1
    BUIC_DEBUG_OFF = 0
    BUIC_DEBUG_ON = 1


class SystemConstants(IntEnum):
    MAX_CFG_PARAMS = 250
    MAX_CFG_STRING_PARAMS = 20
    MAX_PARAMS = 250
