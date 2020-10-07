from main.text import *


def get_main_ctx():
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
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_soon_ctx():
    context = {
        'code': CODE,
        'github_link': GITHUB_SOON,
        'coviduk_link': COVIDUK_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_SOON,
        'title': SOON_TITLE,
        'subtitile': SOON_SUBTITLE,
        'subtitle2': SOON_SUBTITLE2,
        'data_supply': SOON_DATA_SUPPLY,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'in_short_txt': SOON_APP_DESC,
        'in_depth_txt': SOON_APP_DESC_DETAILED,
        'app_goal': SOON_APP_GOAL,
        'app_goal_txt': SOON_APP_GOAL_TXT,
        'app_tech': SOON_TECH,
        'app_tech_txt': SOON_TECH_TXT,
        'data_source': SOON_DATA_SOURCE,
        'data_source_txt': SOON_DATA_SOURCE_TXT,
        'data_source_txt2': SOON_DATA_SOURCE_TXT2,
        'data_source_link': SOON_DATA_SOURCE_LINK,
    }
    ctx = {**get_main_ctx(), **context}
    return ctx



def get_main_coviduk_ctx():
    context = {
        'code': CODE,
        'github_link': GITHUB_PYTHON_PROJ_1,
        'coviduk_link': COVIDUK_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_UK,
        'title': COVID_TITLE,
        'subtitile': COVID_SUBTITLE,
        'subtitle2': COVID_SUBTITLE2,
        'data_supply': COVID_DATA_SUPPLY,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'in_short_txt': COVID_APP_DESC,
        'in_depth_txt': COVID_APP_DESC_DETAILED,
        'app_goal': COVID_APP_GOAL,
        'app_goal_txt': COVID_APP_GOAL_TXT,
        'app_tech': COVID_TECH,
        'app_tech_txt': COVID_TECH_TXT,
        'data_source': COVID_DATA_SOURCE,
        'data_source_txt': COVID_DATA_SOURCE_TXT,
        'data_source_txt2': COVID_DATA_SOURCE_TXT2,
        'data_source_link': COVID_DATA_SOURCE_LINK,
    }

    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_owid_ctx():
    context = {
        'code': CODE,
        'github_link': GITHUB_PYTHON_PROJ_2,
        'app_link': OWID_LINK,
        'app_btn_txt': OWID_APP_BTN_TXT,
        'image': IMAGE_GLOBE,
        'title': OWID_TITLE,
        'subtitile': OWID_SUBTITLE,
        'subtitle2': OWID_SUBTITLE2,
        'data_supply': OWID_DATA_SUPPLY,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'in_short_txt': OWID_APP_DESC,
        'in_depth_txt': OWID_APP_DESC_DETAILED,
        'app_goal': OWID_APP_GOAL,
        'app_goal_txt': OWID_APP_GOAL_TXT,
        'app_tech': OWID_TECH,
        'app_tech_txt': OWID_TECH_TXT,
        'data_source': OWID_DATA_SOURCE,
        'data_source_txt': OWID_DATA_SOURCE_TXT,
        'data_source_txt2': OWID_DATA_SOURCE_TXT2,
        'data_source_link': OWID_DATA_SOURCE_LINK,

    }
    ctx = {**get_main_ctx(), **context}
    return ctx


def get_main_enquiry_ctx():
    context = {
        'code': CODE,
        'github_link': GITHUB_JAVA_PROJ_1,
        'app_link': ENQUIRY_LINK,
        'app_btn_txt': ENQUIRY_APP_BTN_TXT,
        'image': IMAGE_ENQUIRY_1,
        'title': ENQUIRY_TITLE,
        'in_short': IN_SHORT,
        'in_depth': IN_DEPTH,
        'in_short_txt': ENQUIRY_APP_DESC,
        'in_depth_txt': ENQUIRY_APP_DESC_DETAILED,
        'app_goal': ENQUIRY_APP_GOAL,
        'app_goal_txt': ENQUIRY_APP_GOAL_TXT,
        'app_tech': ENQUIRY_TECH,
        'app_tech_txt': ENQUIRY_TECH_TXT,

    }
    ctx = {**get_main_ctx(), **context}
    return ctx