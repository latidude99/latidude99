from main.text import *


def get_base_ctx():
    context = {
        'style_css': STYLE_MAIN,
        'images': IMAGES,
        'code': CODE,
        'github_link': GITHUB,
        'app_btn_txt': APP_BTN_TXT,
        'image': LOGO,
        'title': TITLE,
        'subtitile': SUBTITLE,
        'subtitle2': SUBTITLE2,
        'data_supply': DATA_SUPPLY,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'app_goal': APP_GOAL,
        'app_tech': TECH,
        'app_tech_txt': TECH_TXT,
        'data_source': DATA_SOURCE,
        'data_source_txt': DATA_SOURCE_TXT,
        'data_source_txt2': DATA_SOURCE_TXT2,
        'data_source_link': DATA_SOURCE_LINK,
        'java8': JAVA8,
        'javafx': JAVAFX,
        'javascript': JAVASCRIPT,
        'python3': PYTHON3,
        'django3': DJANGO3,
        'flask': FLASK,
        'mysql5': MYSQL5,
        'nitrodb': NITRODB,
        'bootstrap3': BOOTSTRAP3,
        'bootstrap4': BOOTSTRAP4,
        'spring4': SPRING4,
        'spring5': SPRING5,
        'springboot15': SPRINGBOOT15,
        'springboot2': SPRINGBOOT2,
        'hibernate': HIBERNATE,
        'apachelucene': APACHELUCENE,
        'thymeleaf3': THYMELEAF3,
        'chartsjs': CHARTJS,
        'jcoord': JCOORD,
    }
    return context


def get_main_ctx():
    context = {'footer_info': FOOTER_INFO,
           'background_pattern1': BACKGROUND_PATTERN1,
           'background_pattern2': BACKGROUND_PATTERN2,
           'latidude99': 'latidude99.com',
           'image_piotr': IMAGE_PIOTR,
           'intro1': MAIN_INDEX_INTRO1,
           'intro2': MAIN_INDEX_INTRO2,
           'intro3': MAIN_INDEX_INTRO3,
           'intro4': MAIN_INDEX_INTRO4,
           'home': HOME,
           'nav_java_proj': JAVA_PROJECTS,
           'nav_java_proj_type1': JAVA_PROJ_TYPE_1,
           'nav_java_proj_type2': JAVA_PROJ_TYPE_2,
           'nav_java_proj1': JAVA_PROJ_1,
           'nav_java_proj2': JAVA_PROJ_2,
           'nav_java_proj3': JAVA_PROJ_3,
           'nav_java_proj4': JAVA_PROJ_4,
           'nav_java_proj4a': JAVA_PROJ_4a,
           'nav_java_proj5': JAVA_PROJ_5,
           'nav_java_proj6': JAVA_PROJ_6,
           'nav_java_proj7': JAVA_PROJ_7,
           'nav_python_proj': PYTHON_PROJECTS,
           'nav_python_proj_type1': PYTHON_PROJ_TYPE_1,
           'nav_python_proj_type2': PYTHON_PROJ_TYPE_2,
           'nav_python_proj1': PYTHON_PROJ_1,
           'nav_python_proj2': PYTHON_PROJ_2,
           'nav_android_proj': ANDROID_PROJECTS,
           'nav_android_proj1': ANDROID_PROJ_1,
           'java': JAVA,
           'python': PYTHON,
           'android': ANDROID,
           }
    ctx = {**get_base_ctx(), **context}
    return ctx


def get_index_ctx():
    context = {'title_soon_proj': 'coming soon',
               'title_python_proj_1': TITLE_PYTHON_PROJ_1,
               'desc_python_proj_1': DESC_PYTHON_PROJ_1,
               'github_python_proj_1': GITHUB_PYTHON_PROJ_1,
               'image_python_proj_1': IMAGE_PYTHON_PROJ_1,
               'title_python_proj_2': TITLE_PYTHON_PROJ_2,
               'desc_python_proj_2': DESC_PYTHON_PROJ_2,
               'github_python_proj_2': GITHUB_PYTHON_PROJ_2,
               'image_python_proj_2': IMAGE_PYTHON_PROJ_2,
               'title_java_proj_1': TITLE_JAVA_PROJ_1,
               'desc_java_proj_1': DESC_JAVA_PROJ_1,
               'image_java_proj_1': IMAGE_JAVA_PROJ_1,
               'link_java_proj_1': LINK_JAVA_PROJ_1,
               'github_java_proj_1': GITHUB_JAVA_PROJ_1,
               'title_java_proj_2': TITLE_JAVA_PROJ_2,
               'desc_java_proj_2': DESC_JAVA_PROJ_2,
               'image_java_proj_2': IMAGE_JAVA_PROJ_2,
               'link_java_proj_2': LINK_JAVA_PROJ_2,
               'github_java_proj_2': GITHUB_JAVA_PROJ_2,
               'title_java_proj_3': TITLE_JAVA_PROJ_3,
               'desc_java_proj_3': DESC_JAVA_PROJ_3,
               'image_java_proj_3a': IMAGE_JAVA_PROJ_3a,
               'image_java_proj_3b': IMAGE_JAVA_PROJ_3b,
               'link_java_proj_3': LINK_JAVA_PROJ_3,
               'github_java_proj_3': GITHUB_JAVA_PROJ_3,
               'title_java_proj_4': TITLE_JAVA_PROJ_4,
               'desc_java_proj_4': DESC_JAVA_PROJ_4,
               'image_java_proj_4a': IMAGE_JAVA_PROJ_4a,
               'image_java_proj_4b': IMAGE_JAVA_PROJ_4b,
               'link_java_proj_4': LINK_JAVA_PROJ_4,
               'github_java_proj_4': GITHUB_JAVA_PROJ_4,
               'title_java_proj_5': TITLE_JAVA_PROJ_5,
               'desc_java_proj_5': DESC_JAVA_PROJ_5,
               'image_java_proj_5a': IMAGE_JAVA_PROJ_5a,
               'image_java_proj_5b': IMAGE_JAVA_PROJ_5b,
               'image_java_proj_5c': IMAGE_JAVA_PROJ_5c,
               'link_java_proj_5': LINK_JAVA_PROJ_5,
               'github_java_proj_5': GITHUB_JAVA_PROJ_5,
               'title_java_proj_6': TITLE_JAVA_PROJ_6,
               'desc_java_proj_6': DESC_JAVA_PROJ_6,
               'image_java_proj_6a': IMAGE_JAVA_PROJ_6a,
               'image_java_proj_6b': IMAGE_JAVA_PROJ_6b,
               'link_java_proj_6': LINK_JAVA_PROJ_6,
               'github_java_proj_6': GITHUB_JAVA_PROJ_6,
               'title_android_proj_1': TITLE_ANDROID_PROJ_1,
               'desc_android_proj_1': DESC_ANDROID_PROJ_1,
               'image_android_proj_1a': IMAGE_ANDROID_PROJ_1a,
               'image_android_proj_1b': IMAGE_ANDROID_PROJ_1b,
               'link_android_proj_1': LINK_ANDROID_PROJ_1,
               'github_android_proj_1': GITHUB_ANDROID_PROJ_1,
               }
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_coviduk_ctx():
    context = {
        'github_link': GITHUB_PYTHON_PROJ_1,
        'coviduk_link': COVIDUK_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_UK,
        'title': COVID_TITLE,
        'subtitile': COVID_SUBTITLE,
        'subtitle2': COVID_SUBTITLE2,
        'in_short_txt': COVID_IN_SHORT,
        'in_depth_txt1': COVID_IN_DEPTH1,
        'in_depth_txt2': COVID_IN_DEPTH2,
        'in_depth_txt3': COVID_IN_DEPTH3,
        'in_depth_txt4': COVID_IN_DEPTH4,
        'app_goal_txt': COVID_APP_GOAL,
        'app_tech_txt': COVID_TECH,
        'data_source_txt': COVID_DATA_SOURCE_TXT,
        'data_source_txt2': COVID_DATA_SOURCE_TXT2,
        'data_source_link': COVID_DATA_SOURCE_LINK,
        'image1': IMAGE_COVIDUK_1,
        'image2': IMAGE_COVIDUK_2,
        'image3': IMAGE_COVIDUK_3,
        'image4': IMAGE_COVIDUK_4,
    }

    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_owid_ctx():
    context = {
        'github_link': GITHUB_PYTHON_PROJ_2,
        'app_link': OWID_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_GLOBE,
        'title': OWID_TITLE,
        'subtitile': OWID_SUBTITLE,
        'subtitle2': OWID_SUBTITLE2,
        'data_supply': OWID_DATA_SUPPLY,
        'in_short_txt': OWID_IN_SHORT,
        'app_tech_txt': OWID_TECH,
        'data_source_txt': OWID_DATA_SOURCE_TXT,
        'data_source_txt2': OWID_DATA_SOURCE_TXT2,
        'data_source_link': OWID_DATA_SOURCE_LINK,
        'in_depth_txt1': OWID_IN_DEPTH1,
        'in_depth_txt2': OWID_IN_DEPTH2,
        'in_depth_txt3': OWID_IN_DEPTH3,
        'in_depth_txt4': OWID_IN_DEPTH4,
        'image1': IMAGE_OWID_1,
        'image2': IMAGE_OWID_2,
        'image3': IMAGE_OWID_3,
        'image4': IMAGE_OWID_4,
    }
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_enquiry_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': ENQUIRY_LINK,
        'app_btn_txt': ENQUIRY_APP_BTN_TXT,
        'image': IMAGE_ENQUIRY,
        'title': ENQUIRY_TITLE,
        'in_short_txt': ENQUIRY_IN_SHORT,
        'app_tech_txt': ENQUIRY_TECH,
        'in_depth_txt1': ENQUIRY_IN_DEPTH1,
        'in_depth_txt2': ENQUIRY_IN_DEPTH2,
        'in_depth_txt3': ENQUIRY_IN_DEPTH3,
        'in_depth_txt4': ENQUIRY_IN_DEPTH4,
        'image0': IMAGE_ENQUIRY_0,
        'image1': IMAGE_ENQUIRY_1,
        'image2': IMAGE_ENQUIRY_2,
        'image3': IMAGE_ENQUIRY_3,
        'image4': IMAGE_ENQUIRY_4,
        'image5': IMAGE_ENQUIRY_5,
    }
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_contacts_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': CONTACTS_LINK,
        'app_btn_txt': CONTACTS_APP_BTN_TXT,
        'image': IMAGE_CONTACTS,
        'title': CONTACTS_TITLE,
        'in_short_txt': CONTACTS_IN_SHORT,
        'app_tech_txt': CONTACTS_TECH,
        'in_depth_txt1': CONTACTS_IN_DEPTH1,
        'in_depth_txt2': CONTACTS_IN_DEPTH2,
        'in_depth_txt3': CONTACTS_IN_DEPTH3,
        'in_depth_txt4': CONTACTS_IN_DEPTH4,
        'image1': IMAGE_CONTACTS_1,
        'image2': IMAGE_CONTACTS_1,
        'image3': IMAGE_CONTACTS_1,
        'image4': IMAGE_CONTACTS_1,
        'image5': IMAGE_CONTACTS_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_links_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': LINKS_LINK,
        'app_btn_txt': LINKS_APP_BTN_TXT,
        'image': IMAGE_LINKS,
        'title': LINKS_TITLE,
        'in_short_txt': LINKS_IN_SHORT,
        'app_tech_txt': LINKS_TECH,
        'in_depth_txt1': LINKS_IN_DEPTH1,
        'in_depth_txt2': LINKS_IN_DEPTH2,
        'in_depth_txt3': LINKS_IN_DEPTH3,
        'in_depth_txt4': LINKS_IN_DEPTH4,
        'image1': IMAGE_LINKS_1,
        'image2': IMAGE_LINKS_1,
        'image3': IMAGE_LINKS_1,
        'image4': IMAGE_LINKS_1,
        'image5': IMAGE_LINKS_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx



def get_main_maptools_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': MAPTOOLS_LINK,
        'app_btn_txt': MAPTOOLS_APP_BTN_TXT,
        'image': IMAGE_MAPTOOLS,
        'title': MAPTOOLS_TITLE,
        'in_short_txt': MAPTOOLS_IN_SHORT,
        'app_tech_txt': MAPTOOLS_TECH,
        'in_depth_txt1': MAPTOOLS_IN_DEPTH1,
        'in_depth_txt2': MAPTOOLS_IN_DEPTH2,
        'in_depth_txt3': MAPTOOLS_IN_DEPTH3,
        'in_depth_txt4': MAPTOOLS_IN_DEPTH4,
        'image1': IMAGE_MAPTOOLS_1,
        'image2': IMAGE_MAPTOOLS_1,
        'image3': IMAGE_MAPTOOLS_1,
        'image4': IMAGE_MAPTOOLS_1,
        'image5': IMAGE_MAPTOOLS_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx




def get_main_sncreader_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': SNCREADER_LINK,
        'app_btn_txt': SNCREADER_APP_BTN_TXT,
        'image': IMAGE_SNCREADER,
        'title': SNCREADER_TITLE,
        'in_short_txt': SNCREADER_IN_SHORT,
        'app_tech_txt': SNCREADER_TECH,
        'in_depth_txt1': SNCREADER_IN_DEPTH1,
        'in_depth_txt2': SNCREADER_IN_DEPTH2,
        'in_depth_txt3': SNCREADER_IN_DEPTH3,
        'in_depth_txt4': SNCREADER_IN_DEPTH4,
        'image1': IMAGE_SNCREADER_1,
        'image2': IMAGE_SNCREADER_1,
        'image3': IMAGE_SNCREADER_1,
        'image4': IMAGE_SNCREADER_1,
        'image5': IMAGE_SNCREADER_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx





def get_main_folderbackup_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': FOLDERBACKUP_LINK,
        'app_btn_txt': FOLDERBACKUP_APP_BTN_TXT,
        'image': IMAGE_FOLDERBACKUP,
        'title': FOLDERBACKUP_TITLE,
        'in_short_txt': FOLDERBACKUP_IN_SHORT,
        'app_tech_txt': FOLDERBACKUP_TECH,
        'in_depth_txt1': FOLDERBACKUP_IN_DEPTH1,
        'in_depth_txt2': FOLDERBACKUP_IN_DEPTH2,
        'in_depth_txt3': FOLDERBACKUP_IN_DEPTH3,
        'in_depth_txt4': FOLDERBACKUP_IN_DEPTH4,
        'image1': IMAGE_FOLDERBACKUP_1,
        'image2': IMAGE_FOLDERBACKUP_1,
        'image3': IMAGE_FOLDERBACKUP_1,
        'image4': IMAGE_FOLDERBACKUP_1,
        'image5': IMAGE_FOLDERBACKUP_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx




def get_main_maptoolsapp_ctx():
    context = {
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': MAPTOOLSAPP_LINK,
        'app_btn_txt': MAPTOOLSAPP_APP_BTN_TXT,
        'image': IMAGE_MAPTOOLSAPP,
        'title': MAPTOOLSAPP_TITLE,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'in_short_txt': MAPTOOLSAPP_IN_SHORT,
        'app_tech_txt': MAPTOOLSAPP_TECH,
        'in_depth_txt1': MAPTOOLSAPP_IN_DEPTH1,
        'in_depth_txt2': MAPTOOLSAPP_IN_DEPTH2,
        'in_depth_txt3': MAPTOOLSAPP_IN_DEPTH3,
        'in_depth_txt4': MAPTOOLSAPP_IN_DEPTH4,
        'image1': IMAGE_MAPTOOLSAPP_1,
        'image2': IMAGE_MAPTOOLSAPP_1,
        'image3': IMAGE_MAPTOOLSAPP_1,
        'image4': IMAGE_MAPTOOLSAPP_1,
        'image5': IMAGE_MAPTOOLSAPP_1,


    }
    ctx = {**get_main_ctx(), **context}
    return ctx




