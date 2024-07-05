int a = Int32.Parse(Console.ReadLine());
for(int i = 0; i < a; i++)
{
    String b = Console.ReadLine();
    Console.WriteLine("{0}{1}",(char)b[0],b[b.Length - 1]);
}
