from main.text import *


def get_main_index_ctx():
    ctx = {'footer_info': FOOTER_INFO,
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
    return ctx


def get_main_soon_ctx():
    context = {
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_SOON,
        'title': SOON_TITLE,
        'subtitile': SOON_SUBTITLE,
        'subtitle2': SOON_SUBTITLE2,
        'data_supply': SOON_DATA_SUPPLY,
        'app_desc': SOON_APP_DESC,
        'app_goal': SOON_APP_GOAL,
        'app_goal_txt': SOON_APP_GOAL_TXT,
        'app_tech': SOON_TECH,
        'app_tech_txt': SOON_TECH_TXT,
        'data_source': SOON_DATA_SOURCE,
        'data_source_txt': SOON_DATA_SOURCE_TXT,
        'data_source_txt2': SOON_DATA_SOURCE_TXT2,
        'data_source_link': SOON_DATA_SOURCE_LINK,
    }
    ctx = {**get_main_index_ctx(), **context}
    return ctx


def get_main_owid_ctx():
    context = {
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_GLOBE,
        'title': OWID_TITLE,
        'subtitile': OWID_SUBTITLE,
        'subtitle2': OWID_SUBTITLE2,
        'data_supply': OWID_DATA_SUPPLY,
        'app_desc': OWID_APP_DESC,
        'app_goal': OWID_APP_GOAL,
        'app_goal_txt': OWID_APP_GOAL_TXT,
        'app_tech': OWID_TECH,
        'app_tech_txt': OWID_TECH_TXT,
        'data_source': OWID_DATA_SOURCE,
        'data_source_txt': OWID_DATA_SOURCE_TXT,
        'data_source_txt2': OWID_DATA_SOURCE_TXT2,
        'data_source_link': OWID_DATA_SOURCE_LINK,
    }
    ctx = {**get_main_index_ctx(), **context}
    return ctx


def get_main_coviduk_ctx():
    context = {
        'coviduk_link': COVIDUK_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_UK,
        'title': COVID_TITLE,
        'subtitile': COVID_SUBTITLE,
        'subtitle2': COVID_SUBTITLE2,
        'data_supply': COVID_DATA_SUPPLY,
        'app_desc': COVID_APP_DESC,
        'app_goal': COVID_APP_GOAL,
        'app_goal_txt': COVID_APP_GOAL_TXT,
        'app_tech': COVID_TECH,
        'app_tech_txt': COVID_TECH_TXT,
        'data_source': COVID_DATA_SOURCE,
        'data_source_txt': COVID_DATA_SOURCE_TXT,
        'data_source_txt2': COVID_DATA_SOURCE_TXT2,
        'data_source_link': COVID_DATA_SOURCE_LINK,
    }

    ctx = {**get_main_index_ctx(), **context}
    return ctx
