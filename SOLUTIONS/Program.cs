using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BeginnersProblem2._0
{
    class Program
    {
        static void Main(string[] args)
        {
            var numberofTestCases = int.Parse(Console.ReadLine());
            var resultsArray = new int[numberofTestCases];
            for(var i = 0; i < numberofTestCases; i++)
            {
                var numberofTestableValues = int.Parse(Console.ReadLine());
                var testableValues = new int[numberofTestableValues];

                var testableValuesStringArray = Console.ReadLine().Split(' ');

                for(var j = 0; j< numberofTestableValues; j++)
                {
                    testableValues[j] = int.Parse(testableValuesStringArray[j]);
                }
                resultsArray[i] = findFrequencyofBestValues(testableValues);
            }

            foreach(var result in resultsArray)
            {
                Console.WriteLine(result);
            }
        }

        private static int findFrequencyofBestValues(int [] testableValues)
        {
            var frequency = 0;
            foreach(var testValue in testableValues)
            {
                if(testValue % 2 == 0)
                {
                    frequency++;
                }
            }
            return frequency;
        }
    }
}
