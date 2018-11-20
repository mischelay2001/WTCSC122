# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GolfCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolfCourse'
        verbose_name = "Golf Course"
        verbose_name_plural = "Golf Courses"

    def getParList(self):
        # 1. Retrieve a queryset list of the Hole objects from the database, filtered to only get the Hole objects,
        # whose hole_course_id matches the GolfCourse course_id. This
        holes = Hole.objects.filter(hole_course_id=self.course_id)
        # 2. Create an empty list to hold Hole par values.
        hole_par_scores = list()
        # 3. Using a for loop, traverse the list of Hole objects returned from, the first step – for hole in holes:
        # - and in the loop append the hole par value (hole.hole_par) to the empty list created in step 2.
        for hole in holes:
            hole_par_scores.append(hole.hole_par)
        # 4. Return the list filled in step 3.
        return hole_par_scores

    def __str__(self):
        return self.course_name


class Hole(models.Model):
    hole_id = models.AutoField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Hole'

    def __str__(self):
        return "{}, Hole {}, Par {}".format(self.hole_course.course_name,
                                            self.hole_number, self.hole_par)
