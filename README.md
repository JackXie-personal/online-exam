
```
Online-Examination-System-master
├─ .DS_Store
├─ .all-contributorsrc
├─ .env
├─ Exam
│  ├─ .DS_Store
│  ├─ admission
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_auto_20240306_2225.py
│  │  │  ├─ 0003_auto_20240306_2228.py
│  │  │  ├─ 0004_auto_20240309_1917.py
│  │  │  ├─ 0005_auto_20240309_1919.py
│  │  │  ├─ 0006_delete_locality.py
│  │  │  ├─ 0007_auto_20240317_0327.py
│  │  │  ├─ 0008_auto_20240317_0343.py
│  │  │  ├─ 0009_applicant_registration_gender.py
│  │  │  ├─ 0010_auto_20240330_1432.py
│  │  │  ├─ 0011_department_nationality_student_village.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  └─ admission
│  │  │     ├─ admission_granted.html
│  │  │     ├─ upload_excel.html
│  │  │     └─ upload_success.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ course
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ db.sqlite3
│  ├─ examProject
│  │  ├─ .DS_Store
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ static
│  │  │  ├─ .DS_Store
│  │  │  ├─ css
│  │  │  │  ├─ bootstrap.min.css
│  │  │  │  ├─ dashboard.css
│  │  │  │  └─ main.css
│  │  │  ├─ img
│  │  │  │  ├─ about.jpg
│  │  │  │  ├─ book.png
│  │  │  │  ├─ ems.jpg
│  │  │  │  ├─ exam.jpg
│  │  │  │  ├─ login.jpg
│  │  │  │  └─ registration.jpg
│  │  │  └─ js
│  │  │     ├─ bootstrap.bundle.min.js
│  │  │     └─ register.js
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ wsgi.py
│  ├─ faculty
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ manage.py
│  ├─ media
│  │  ├─ faculty_profile_pics
│  │  │  ├─ 128706.png
│  │  │  ├─ 128706_Kpn9Mj5.png
│  │  │  ├─ 205913.jpg
│  │  │  ├─ 653531.jpg
│  │  │  └─ wallpaperflare.com_wallpaper_1.jpg
│  │  └─ student_profile_pics
│  │     └─ QiFPVPE.jpg
│  ├─ questions
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_auto_20201201_1214.py
│  │  │  ├─ 0003_auto_20201201_1604.py
│  │  │  ├─ 0004_auto_20201202_1703.py
│  │  │  ├─ 0005_auto_20201202_1703.py
│  │  │  ├─ 0006_auto_20201202_1753.py
│  │  │  ├─ 0007_auto_20201202_1911.py
│  │  │  ├─ 0008_auto_20201202_1912.py
│  │  │  ├─ 0009_auto_20201202_1912.py
│  │  │  ├─ 0010_auto_20201202_1916.py
│  │  │  ├─ 0011_auto_20201203_1518.py
│  │  │  ├─ 0012_auto_20201204_2046.py
│  │  │  ├─ 0012_auto_20201205_0811.py
│  │  │  ├─ 0013_auto_20201204_2047.py
│  │  │  ├─ 0013_auto_20201205_0811.py
│  │  │  ├─ 0014_auto_20201218_0833.py
│  │  │  ├─ 0015_auto_20201218_0833.py
│  │  │  ├─ 0016_auto_20201218_0843.py
│  │  │  ├─ 0017_merge_20210127_1143.py
│  │  │  ├─ 0018_auto_20210212_2310.py
│  │  │  ├─ 0019_auto_20210408_0915.py
│  │  │  ├─ 0020_auto_20210408_1052.py
│  │  │  ├─ 0021_auto_20210408_1052.py
│  │  │  ├─ 0022_auto_20240330_1421.py
│  │  │  ├─ 0023_auto_20240330_1432.py
│  │  │  ├─ 0024_auto_20240408_1212.py
│  │  │  ├─ 0025_auto_20240409_1155.py
│  │  │  ├─ 0026_auto_20240409_1748.py
│  │  │  ├─ 0027_auto_20240409_1818.py
│  │  │  ├─ 0028_auto_20240409_1929.py
│  │  │  ├─ 0029_auto_20240409_2013.py
│  │  │  ├─ 0030_alter_exam_model_end_time_and_more.py
│  │  │  ├─ 0031_remove_question_db_answer_and_more.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ question_models.py
│  │  ├─ questionpaper_models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ resultprocessing
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_auto_20240409_1748.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ student
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ api.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_stu_question_stuexam_db_sturesults_db.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ utils.py
│  │  └─ views.py
│  ├─ studentPreferences
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ templates
│  │  ├─ base.html
│  │  ├─ base_auth.html
│  │  ├─ base_faculty.html
│  │  ├─ exam
│  │  │  ├─ addquestionpaper.html
│  │  │  ├─ addquestions.html
│  │  │  ├─ attendance.html
│  │  │  ├─ giveExam.html
│  │  │  ├─ mainexam.html
│  │  │  ├─ mainexamstudent.html
│  │  │  ├─ previousexam.html
│  │  │  ├─ previousstudent.html
│  │  │  ├─ result.html
│  │  │  ├─ resultsstudent.html
│  │  │  └─ viewstudents.html
│  │  ├─ faculty
│  │  │  ├─ index.html
│  │  │  ├─ login.html
│  │  │  ├─ register.html
│  │  │  ├─ resetPassword.html
│  │  │  ├─ resetPasswordDone.html
│  │  │  ├─ resetPasswordSent.html
│  │  │  └─ setNewPassword.html
│  │  ├─ homepage.html
│  │  ├─ partials
│  │  │  ├─ _messages.html
│  │  │  ├─ _sidebar.html
│  │  │  └─ _sidebar_faculty.html
│  │  ├─ result
│  │  │  ├─ program_result_sheet.html
│  │  │  └─ student_results.html
│  │  ├─ resultprocessing
│  │  │  └─ final_year_result_sheet.html
│  │  ├─ static
│  │  │  ├─ css
│  │  │  │  └─ styles.css
│  │  │  └─ js
│  │  │     └─ scripts.js
│  │  ├─ student
│  │  │  ├─ index.html
│  │  │  ├─ login.html
│  │  │  ├─ register.html
│  │  │  ├─ resetPassword.html
│  │  │  ├─ resetPasswordDone.html
│  │  │  ├─ resetPasswordSent.html
│  │  │  └─ setNewPassword.html
│  │  └─ studentPreferences
│  │     ├─ change_password.html
│  │     └─ pref.html
│  └─ tuition
│     ├─ __init__.py
│     ├─ admin.py
│     ├─ apps.py
│     ├─ migrations
│     │  ├─ 0001_initial.py
│     │  └─ __init__.py
│     ├─ models.py
│     ├─ templates
│     │  └─ tuition
│     │     ├─ error.html
│     │     ├─ result.html
│     │     └─ success.html
│     ├─ tests.py
│     ├─ urls.py
│     └─ views.py
├─ Pipfile
├─ Pipfile.lock
└─ requirements.txt

```