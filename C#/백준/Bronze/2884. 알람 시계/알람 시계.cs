String[] n = Console.ReadLine().Split();
int a = Convert.ToInt32(n[0]), b = Convert.ToInt32(n[1]);

Console.Write((b - 45 >= 0 ? a : (a != 0 ? a - 1 : 23) )+ " " + (b - 45 >= 0 ? b - 45 : b - 45 + 60));