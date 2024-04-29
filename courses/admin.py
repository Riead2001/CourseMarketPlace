from django.contrib import admin
from courses.models import Course
from courses.models import Tag, Learning, Prerequisite, Video, UserCourse, Payment

from courses.templatetags.course_custom_tag import apply_discount
from django.utils.html import format_html
from .models.result import Marks # Import the Result model
from courses.models.scholarship import Scholarship


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from courses.models.rating import Rating

from courses.models import Quiz



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'education', 'college_name', 'role')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('role',)




class RatingAdmin(admin.ModelAdmin):
    list_display = ('username', 'coursename', 'rating', 'review')
    list_filter = ('coursename',)
    search_fields = ('username__username', 'coursename')

admin.site.register(Rating, RatingAdmin)



admin.site.register(CustomUser, CustomUserAdmin)

class TagAdmin(admin.TabularInline):
    model = Tag


class VideoAdmin(admin.TabularInline):
    model = Video


class LearningAdmin(admin.TabularInline):
    model = Learning


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, VideoAdmin, LearningAdmin, PrerequisiteAdmin]
    list_display = ['name', 'user_mode', 'get_price', 'get_discount', 'buying_price', 'active']
    list_filter = ['price', 'discount']
    list_editable = ['active'] 

    def get_price(self, course):
        return f'₹ {course.price}'

    def get_discount(self, course):
        return f'{course.discount} %'

    def buying_price(self, course):
        return f'₹ {apply_discount(course.price, course.discount)}'
    

    def user_mode(self, course):
        return format_html(f'<a target="_blank" href="/course/{course.slug}/">Open in User Mode</a>')

    get_price.short_description = 'Price'
    get_discount.short_description = 'Discount'







class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_course']

    def get_course(self, video):
        return format_html(f'<a href="/admin/courses/course/{video.course.id}/">{video.title}</a>')





class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'get_user', 'get_course', 'status')
    list_filter = ('status', 'time')
    list_editable = ['status'] 


    def get_user(self, payment):
        return format_html(f'<a href="/admin/auth/user/{payment.user.id}">{payment.user}</a>')

    def get_course(self, payment):
        return format_html(f'<a href="/admin/courses/course/{payment.course.id}">{payment.course}</a>')

        
    get_user.short_description = 'User'
    get_course.short_description = 'Course'





class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('open', 'get_user', 'get_course')
    list_filter = ('course',)

    def open(self, user_course):
        return 'Click to open'

    def get_user(self, user_course):
        return format_html(f'<a href="/admin/auth/user/{user_course.user.id}/">{user_course.user}</a>')

    def get_course(self, user_course):
        return format_html(f'<a href="/admin/courses/course/{user_course.course.id}/">{user_course.course}</a>')

        
    get_user.short_description = 'User'
    get_course.short_description = 'Course'



# Define your other admin classes here...

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz_mark', 'assignment_mark', 'total_mark', 'student')  # Define the fields you want to display in the list view
    list_filter = ('student',)  # Add any filters you want to apply
    search_fields = ['student__name']  # Add fields you want to search on

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('username', 'coursename', 'reason', 'description')  # Define the fields you want to display in the list view

from django.contrib import admin
from courses.models.demopay import DemoPay

@admin.register(DemoPay)
class DemoPayAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_name')
admin.register(DemoPayAdmin)


admin.site.register(Marks, ResultAdmin) 
admin.site.register(Scholarship, ScholarshipAdmin) 

admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Payment, PaymentAdmin)


admin.site.register(Quiz)