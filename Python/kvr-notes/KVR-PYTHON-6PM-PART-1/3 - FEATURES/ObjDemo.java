class Student
{
	int sno;
	String sname;
	float marks;
}
class ObjDemo 
{
	public static void main(String[] args) 
	{
		Student s=new Student();
		s.sno=10;
		s.sname="KVR";
		s.marks=22.22f;
		System.out.println(s.sno+" "+s.sname+"  "+s.marks);
		s.cname="OUCET";
	}
}
