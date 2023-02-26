# Generated by Django 3.2.9 on 2021-12-19 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_author_patronymic_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="program",
            options={
                "verbose_name": "тематичкский план форма занятий",
                "verbose_name_plural": "тематичкский план форма занятие",
            },
        ),
        migrations.AlterModelOptions(
            name="thematicplan",
            options={"verbose_name": "тематический план", "verbose_name_plural": "тематические планы"},
        ),
        migrations.AlterField(
            model_name="author",
            name="academic_degree",
            field=models.CharField(
                choices=[("К.Н", "К.Н"), ("Д.Н", "Д.Н")], max_length=8, verbose_name="ученная степень"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="academic_position",
            field=models.CharField(
                choices=[
                    ("аспирант", "аспирант"),
                    ("преподаватель", "преподаватель"),
                    ("доцент", "доцент"),
                    ("профессор", "профессор"),
                ],
                max_length=15,
                verbose_name="должность",
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="academic_tittle",
            field=models.CharField(
                choices=[("доцент", "доцент"), ("профессор", "профессор")],
                max_length=15,
                verbose_name="ученое название",
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="cathedra",
            field=models.CharField(max_length=120, verbose_name="кафедра"),
        ),
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(max_length=120, verbose_name="почта"),
        ),
        migrations.AlterField(
            model_name="author",
            name="first_name",
            field=models.CharField(max_length=120, verbose_name="имя"),
        ),
        migrations.AlterField(
            model_name="author",
            name="institute",
            field=models.CharField(max_length=120, verbose_name="институт"),
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(max_length=120, verbose_name="фамилия"),
        ),
        migrations.AlterField(
            model_name="author",
            name="patronymic_name",
            field=models.CharField(max_length=120, null=True, verbose_name="отчество"),
        ),
        migrations.AlterField(
            model_name="author",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.program", verbose_name="программа"
            ),
        ),
        migrations.AlterField(
            model_name="competence",
            name="cipher",
            field=models.CharField(max_length=5, verbose_name="шифр"),
        ),
        migrations.AlterField(
            model_name="competence",
            name="name",
            field=models.CharField(max_length=300, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="curriculum",
            name="exam",
            field=models.BooleanField(default=False, verbose_name="экзамен"),
        ),
        migrations.AlterField(
            model_name="curriculum",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.profile", verbose_name="профиль"
            ),
        ),
        migrations.AlterField(
            model_name="curriculum",
            name="program_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.programname", verbose_name="названия программа"
            ),
        ),
        migrations.AlterField(
            model_name="curriculum",
            name="semester_number",
            field=models.JSONField(default=list, verbose_name="семестер"),
        ),
        migrations.AlterField(
            model_name="curriculum",
            name="test",
            field=models.BooleanField(default=False, verbose_name="тест"),
        ),
        migrations.AlterField(
            model_name="curriculumlessonform",
            name="count",
            field=models.IntegerField(verbose_name="количество"),
        ),
        migrations.AlterField(
            model_name="curriculumlessonform",
            name="curriculum",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.curriculum", verbose_name="учебный план"
            ),
        ),
        migrations.AlterField(
            model_name="curriculumlessonform",
            name="lesson_form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.lessonform", verbose_name="форма занятия"
            ),
        ),
        migrations.AlterField(
            model_name="direction",
            name="name",
            field=models.CharField(max_length=120, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="direction",
            name="number",
            field=models.CharField(max_length=20, verbose_name="номер"),
        ),
        migrations.AlterField(
            model_name="direction",
            name="qualification",
            field=models.CharField(
                choices=[("BACHELOR", "Бакалавриат"), ("MASTER", "Магистратура")],
                max_length=20,
                verbose_name="квалификация",
            ),
        ),
        migrations.AlterField(
            model_name="internetresource",
            name="link",
            field=models.URLField(max_length=120, verbose_name="ссылка"),
        ),
        migrations.AlterField(
            model_name="internetresource",
            name="name",
            field=models.CharField(max_length=120, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="internetresource",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.program", verbose_name="программа"
            ),
        ),
        migrations.AlterField(
            model_name="lessonform",
            name="name",
            field=models.CharField(max_length=120, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="lessonform",
            name="text",
            field=models.TextField(verbose_name="текст"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="direction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.direction", verbose_name="направления"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(max_length=120, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="program",
            name="accounting_methodological_support",
            field=models.TextField(null=True, verbose_name="методическое обеспечение бухгалтерского учета"),
        ),
        migrations.AlterField(
            model_name="program",
            name="capabilities",
            field=models.TextField(null=True, verbose_name="возможности"),
        ),
        migrations.AlterField(
            model_name="program",
            name="form_training",
            field=models.CharField(
                choices=[("руский", "руский"), ("англиский", "англиский")], max_length=20, verbose_name="форма обучения"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="language_choices",
            field=models.CharField(
                choices=[("руский", "руский"), ("англиский", "англиский")], max_length=20, verbose_name="язык"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="material_technical_base",
            field=models.TextField(verbose_name="материально-техническая база"),
        ),
        migrations.AlterField(
            model_name="program",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.profile", verbose_name=" профиль"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="program_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.programname", verbose_name="название программы"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="release_date",
            field=models.DateField(verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="program",
            name="type_discipline",
            field=models.CharField(
                choices=[("вазовая", "вазовая"), ("вариативная", "вариативная"), ("курс по вибору", "курс по вибору")],
                max_length=20,
                verbose_name="тип дисциплина",
            ),
        ),
        migrations.AlterField(
            model_name="programname",
            name="name",
            field=models.CharField(max_length=120, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="studentmust",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.program", verbose_name="программа"
            ),
        ),
        migrations.AlterField(
            model_name="studentmust",
            name="text",
            field=models.TextField(verbose_name="текст"),
        ),
        migrations.AlterField(
            model_name="studentmust",
            name="text_choices",
            field=models.CharField(
                choices=[("знать", "знать"), ("уметь", "уметь"), ("владеть", "владеть")],
                max_length=8,
                verbose_name="тип текста",
            ),
        ),
        migrations.AlterField(
            model_name="thematicplan",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.program", verbose_name="программа"
            ),
        ),
        migrations.AlterField(
            model_name="thematicplan",
            name="semester_number",
            field=models.IntegerField(verbose_name="семестер"),
        ),
        migrations.AlterField(
            model_name="thematicplan",
            name="text",
            field=models.TextField(verbose_name="текст"),
        ),
        migrations.AlterField(
            model_name="thematicplan",
            name="theme",
            field=models.CharField(max_length=120, verbose_name="тема"),
        ),
        migrations.AlterField(
            model_name="thematicplanformlesson",
            name="count",
            field=models.IntegerField(verbose_name="количество форма занятие"),
        ),
        migrations.AlterField(
            model_name="thematicplanformlesson",
            name="lesson_form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.lessonform", verbose_name="форма занятия"
            ),
        ),
        migrations.AlterField(
            model_name="thematicplanformlesson",
            name="thematic_plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.thematicplan", verbose_name="тематический план"
            ),
        ),
    ]
