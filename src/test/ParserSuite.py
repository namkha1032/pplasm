import unittest
from TestUtils import TestParser

testcaseArray = [   # testcase 200-207: Variable and Array declarations
                    """x: integer = 1;""",
                    """y: float = 10.3;""",
                    """flag: boolean = false;""",
                    """newArr: array = array[4,5,6] of float;""",
                    """autoVar: auto = 123;""",
                    """a,b,c : float = 10.3, 20.2, 5.678;""",
                    """arr1, arr2, arr3: array = array[1,2] of integer, array[2,3] of float, array[4,5,6] of string;""",
                    """str1, str2, str3: string = "kha", "dep", "trai";""",

                    # testcase 208-215: Function declarations
                    """print: function integer (){}""",
                    """add: function integer(a:integer, b:integer){
                            return a+b;
                    }""",
                    """foo: function void(x: integer){
                            if(x>=10)
                                print("kha dep trai");
                            else{
                                if(x%2==0)
                                    print("kha xau trai");
                                else{
                                    print("kha vjp pro");
                                    print("kha dep trai x10");
                                }
                            }
                    }""",
                    """ageCalculate: function integer(){
                            print("nhap so tuoi cua ban: ");
                            ageVar = readInput();
                            print("so tuoi cua ban la: ", ageVar);
                    }""",
                    """fact: function integer (n: integer){
                        if (n==0)
                            return 1;
                        else
                            return n*fact(n-1);
                    }""",
                    """simpleFunc1: function auto(){
                        return 1+1;
                    }""",
                    """simpleFunc2: function void(){
                        print("hehehe");
                    }""",
                    """a: integer = 2;
                       b: integer = 3;
                       mulfunc: function integer(x: integer, y: integer){
                            return x*y;
                    }""",

                    # Testcase 216-223: Assign statement
                    """x=2;""",
                    """kha="deptrai";""",
                    """arr[0,1]=6.9;""",
                    """varA = varB;""",
                    """cars = {"honda","toyota","nissan"};""",
                    """myCar = cars[1];""",
                    """result = calculate(a, b);""",
                    """flag = false;""",

                    # Testcase 224-231: If statement
                    """if(thoiTietHomNay == "mua")
                            nghiHoc();""",
                    """if(thoiTietHomNay == "nang")
                            nghiHoc();""",
                    """if(emDongY == true)
                            print("To tinh thanh cong");
                        else
                            print("Mai lam ban nhe");
                        """,
                    """if(a || b){
                        if(a)
                            print(a);
                        else
                            print(c);
                        }
                        else
                        print(d);""",
                    """if(today < deadline)
                            hanNop = "dunghan";
                        else
                            hanNop = "trehan";
                    """,
                    """if(!troimua)
                            diBay();""",
                    """if(a%2==0)
                            print("a la so chan");
                        else
                            print("a la so le");""",
                    """if(1==2)
                            print("kho bau one piece");
                    """,

                    #Testcase 232-239: For statement
                    """for(x=1, x<=100, x+1){
                        print("chep phat 100 lan");
                    }
                    """,
                    """for(i=1, i<=10,i+1)
                        chayMotVongSanTruong();
                    """,
                    """for(i=0, i < arrayLength, i+1){
                            arr[i]=arr[i]*2;
                    }
                    """,
                    """for(i=0, i < verticalSize, i+1){
                            for(j=0, j < horizontalSize, j+1)
                                arr[i, j] = 13; 
                            
                    }""",
                    """for(i = 0, i < 100, i+1){
                            if(i%2==0)
                                print(i);
                    }
                    """,
                    """for(i=0,i<100,i+1){
                            if(i%2==0)
                                continue;
                            print(i);
                    }""",
                    """for(i=100, i > 0, i-1){
                            doSomething();
                    }""",
                    """for(i=0,i<69,i+1){
                            doAnotherThing();
                    }""",

                    #Testcase 240 - 247: While statement
                    """while(true)
                            diNgu();""",
                    """while(x>0){
                        print("i love you");
                        x = x - 1;
                    }""",
                    """while(x<100){
                        if(x%2==0)
                            continue;
                        print(x);
                        x=x+1;
                    }""",
                    """while(a!=b){
                        a = arr[x];
                        b = arr[arrSize-x];
                    }""",
                    """while(a<100){
                            while(b<100){
                                arr[a,b] = 10;
                                b = b+1;
                            }
                            a = a + 1;
                    }""",
                    """while(!flag){
                            print("world cup");
                    }""",
                    """while(state)
                            funcCall();
                        while(taste)
                            callFunc();
                    """,
                    """while(mood == "happy"){
                            study();
                    }""",

                    # Testcase 248 - 255: do-while
                    """do{sleep();}
                        while(everybodyStudying());""",
                    """do{
                            study();
                            eat();
                            x = 1;
                    }while(everybodySleeping());""",
                    """do{
                            x = x + 1;
                    }while (x<100);""",
                    """do{
                            dostuff();
                    }
                    while(homeAlone == true);""",
                    """do{
                            toInfinity();
                    }while(flag == true); """,
                    """do{
                        laugh();
                        eat();
                        hehe = 123;
                    } while(hotFood);""",
                    """do{
                        takeExercise();
                        x = a + b;
                        print(x);
                    }while(systemLoading);""",
                    """do{
                        wakeUp();

                    }while(!troiToi);""",

                    #Test 256 - 263: Break statement
                    """for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            break;
                    }""",
                    """while(i<100){
                        print(i);
                        if(i==a)
                            break;
                    }""",
                    """do{
                            print(i);
                            if(i==a)
                                break;
                    }while(i<100);""",
                    """for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            break;
                    }""",
                    """while(x<100){
                        print(x);
                        if(x==a)
                            break;
                    }""",
                    """do{
                            print(x);
                            if(x==a)
                                break;
                    }while(y<100);""",
                    """for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            break;
                    }""",
                    """while(y<100){
                        print(y);
                        if(y==a)
                            break;
                    }""",

                    # Test 264 - 271: Continue statement
                    """for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            continue;
                    }""",
                    """while(i<100){
                        print(i);
                        if(i==a)
                            continue;
                    }""",
                    """do{
                            print(i);
                            if(i==a)
                                continue;
                    }while(i<100);""",
                    """for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            continue;
                    }""",
                    """while(x<100){
                        print(x);
                        if(x==a)
                            continue;
                    }""",
                    """do{
                            print(x);
                            if(x==a)
                                continue;
                    }while(y<100);""",
                    """for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            continue;
                    }""",
                    """while(y<100){
                        print(y);
                        if(y==a)
                            continue;
                    }""",

                    #Test 272 - 279: Return statement:
                    """intFunc1: function integer(a: integer, b:integer){
                        return a + b;
                    }""",
                    """floatFunc1: function float(a: float, b:float){
                        return a * b;
                    }""",
                    """autoFunc1: function auto(a: string, b: string){
                        return a::b;
                    }""",
                    """intFunc2: function integer(a: integer, b:integer){
                        return a + b;
                    }""",
                    """floatFunc2: function float(a: float, b:float){
                        return a * b;
                    }""",
                    """autoFunc2: function auto(a: string, b: string){
                        return a::b;
                    }""",
                    """intFunc3: function integer(a: integer, b:integer){
                        return a + b;
                    }""",
                    """floatFunc3: function float(a: float, b:float){
                        return a * b;
                    }""",

                    #Test 280 - 287: Call statement:
                    """addAndPrint(a,b);""",
                    """mulAndPrint(a,b);""",
                    """subAndPrint(a,b);""",
                    """divAndPrint(a,b);""",
                    """print("kha dep trai");""",
                    """goo();""",
                    """printFraction(2,3);""",
                    """sleep();""",

                    #Test 288 - 295: Block statement:
                    """{
                            doSomething();
                            add();
                            sleep();
                        }""",
                    """{
                            x: integer = 1;
                            a: integer = 2;
                            b: integer;
                            b = a + x;
                        }""",
                    """{
                            add(1,2);
                            sleep();
                        }""",
                    """{
                        if(troiNang == true){
                            rangoaichoi();
                        }
                    }""",
                    """{
                        getCookie();
                        drinkMilk();
                    }""",
                    """{
                        getCookie();
                        drinkMilk();
                    }""",
                    """{
                        print("hehehe", my);
                    }""",
                    """{
                        foo(a,b);
                    }"""
                ]

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        testcaseNo = 200
        for testcase in testcaseArray:
            self.assertTrue(TestParser.test(testcase, "successful", testcaseNo))
            testcaseNo+=1
