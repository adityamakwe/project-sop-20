import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SignupComponent } from './login/signup.component';
import { LoginComponent } from './login/login.component';
import { UserComponent } from './user/user.component';
import { RoleComponent } from './role/role.component';
import { CollegeComponent } from './college/college.component';
import { CourseComponent } from './course/course.component';
import { SubjectComponent } from './subject/subject.component';
import { MarksheetComponent } from './marksheet/marksheet.component';
import { TimetableComponent } from './timetable/timetable.component';
import { FacultyComponent } from './faculty/faculty.component';
import { StudentComponent } from './student/student.component';
import { UserListComponent } from './user/user-list.component';
import { RoleListComponent } from './role/role-list.component';
import { CollegeListComponent } from './college/college-list.component';
import { CourseListComponent } from './course/course-list.component';
import { SubjectListComponent } from './subject/subject-list.component';
import { FacultyListComponent } from './faculty/faculty-list.component';
import { MarksheetListComponent } from './marksheet/marksheet-list.component';
import { StudentListComponent } from './student/student-list.component';
import { TimetableListComponent } from './timetable/timetable-list.component';


const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'dashboard'
  },
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  {
    path: 'user',
    component: UserComponent
  },
  {
    path: 'role',
    component: RoleComponent
  },
  {
    path: 'college',
    component: CollegeComponent
  },
  {
    path: 'course',
    component: CourseComponent
  },
  {
    path: 'subject',
    component: SubjectComponent
  },
  {
    path: 'marksheet',
    component: MarksheetComponent
  },
  {
    path: 'timetable',
    component: TimetableComponent
  },
  {
    path: 'faculty',
    component: FacultyComponent
  },
  {
    path: 'student',
    component: StudentComponent
  },
  {
    path: 'userlist',
    component: UserListComponent
  },
  {
    path: 'rolelist',
    component:RoleListComponent
  },
  {
    path: 'collegelist',
    component: CollegeListComponent
  },
  {
    path: 'courselist',
    component: CourseListComponent
  },
  {
    path: 'subjectlist',
    component: SubjectListComponent
  },
  {
    path: 'facultylist',
    component: FacultyListComponent
  },
  {
    path: 'marksheetlist',
    component: MarksheetListComponent
  },
  {
    path: 'studentlist',
    component:StudentListComponent
  },
  {
    path: 'timetablelist',
    component:TimetableListComponent
  }
  
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
