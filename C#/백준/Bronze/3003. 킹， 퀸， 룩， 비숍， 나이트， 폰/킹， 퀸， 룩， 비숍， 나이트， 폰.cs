string[] arr1 = Console.ReadLine().Split();
int[] setting = { 1, 1, 2, 2, 2, 8 };
for (int i = 0; i < arr1.Length; i++)
    Console.Write((setting[i] - int.Parse(arr1[i])) + " ");