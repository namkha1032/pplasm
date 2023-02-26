import unittest
from TestUtils import TestParser

testcaseArray = [   # Testcase 200 - 207: Variable and Array declarations
                    ["""x: integer = 1;""","successful"],
                    ["""y: float = 10.3;""","successful"],
                    ["""flag: boolean = false;""","successful"],
                    ["""newArr: array = array[4,5,6] of float;""","successful"],
                    ["""autoVar: auto = 123;""","successful"],
                    ["""a,b,c : float = 10.3, 20.2, 5.678;""","successful"],
                    ["""arr1, arr2, arr3: array = array[1,2] of integer, array[2,3] of float, array[4,5,6] of string;""","successful"],
                    ["""str1, str2, str3: string = "kha", "dep", "trai";""","successful"],

                    # Testcase 208 - 215: Function declarations
                    ["""print: function integer (){}""","successful"],
                    ["""add: function integer(a:integer, b:integer){
                            return a+b;
                    }""","successful"],
                    ["""foo: function void(x: integer){
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
                    }""","successful"],
                    ["""ageCalculate: function integer(){
                            print("nhap so tuoi cua ban: ");
                            ageVar = readInput();
                            print("so tuoi cua ban la: ", ageVar);
                    }""","successful"],
                    ["""fact: function integer (n: integer){
                        if (n==0)
                            return 1;
                        else
                            return n*fact(n-1);
                    }""","successful"],
                    ["""simpleFunc1: function auto(){
                        return 1+1;
                    }""","successful"],
                    ["""simpleFunc2: function void(){
                        print("hehehe");
                    }""","successful"],
                    ["""a: integer = 2;
                       b: integer = 3;
                       mulfunc: function integer(x: integer, y: integer){
                            return x*y;
                    }""","successful"],

                    # Testcase 216 - 223: Assign statement
                    ["""x=2;""","successful"],
                    ["""kha="deptrai";""","successful"],
                    ["""arr[0,1]=6.9;""","successful"],
                    ["""varA = varB;""","successful"],
                    ["""cars = {"honda","toyota","nissan"};""","successful"],
                    ["""myCar = cars[1];""","successful"],
                    ["""result = calculate(a, b);""","successful"],
                    ["""flag = false;""","successful"],

                    # Testcase 224 - 231: If statement
                    ["""if(thoiTietHomNay == "mua")
                            nghiHoc();""","successful"],
                    ["""if(thoiTietHomNay == "nang")
                            nghiHoc();""","successful"],
                    ["""if(emDongY == true)
                            print("To tinh thanh cong");
                        else
                            print("Mai lam ban nhe");
                        ""","successful"],
                    ["""if(a || b){
                        if(a)
                            print(a);
                        else
                            print(c);
                        }
                        else
                        print(d);""","successful"],
                    ["""if(today < deadline)
                            hanNop = "dunghan";
                        else
                            hanNop = "trehan";
                    ""","successful"],
                    ["""if(!troimua)
                            diBay();""","successful"],
                    ["""if(a%2==0)
                            print("a la so chan");
                        else
                            print("a la so le");""","successful"],
                    ["""if(1==2)
                            print("kho bau one piece");
                    ""","successful"],

                    #Testcase 232 - 239: For statement
                    ["""for(x=1, x<=100, x+1){
                        print("chep phat 100 lan");
                    }
                    ""","successful"],
                    ["""for(i=1, i<=10,i+1)
                        chayMotVongSanTruong();
                    ""","successful"],
                    ["""for(i=0, i < arrayLength, i+1){
                            arr[i]=arr[i]*2;
                    }
                    ""","successful"],
                    ["""for(i=0, i < verticalSize, i+1){
                            for(j=0, j < horizontalSize, j+1)
                                arr[i, j] = 13; 
                            
                    }""","successful"],
                    ["""for(i = 0, i < 100, i+1){
                            if(i%2==0)
                                print(i);
                    }
                    ""","successful"],
                    ["""for(i=0,i<100,i+1){
                            if(i%2==0)
                                continue;
                            print(i);
                    }""","successful"],
                    ["""for(i=100, i > 0, i-1){
                            doSomething();
                    }""","successful"],
                    ["""for(i=0,i<69,i+1){
                            doAnotherThing();
                    }""","successful"],

                    #Testcase 240 - 247: While statement
                    ["""while(true)
                            diNgu();""","successful"],
                    ["""while(x>0){
                        print("i love you");
                        x = x - 1;
                    }""","successful"],
                    ["""while(x<100){
                        if(x%2==0)
                            continue;
                        print(x);
                        x=x+1;
                    }""","successful"],
                    ["""while(a!=b){
                        a = arr[x];
                        b = arr[arrSize-x];
                    }""","successful"],
                    ["""while(a<100){
                            while(b<100){
                                arr[a,b] = 10;
                                b = b+1;
                            }
                            a = a + 1;
                    }""","successful"],
                    ["""while(!flag){
                            print("world cup");
                    }""","successful"],
                    ["""while(state)
                            funcCall();
                        while(taste)
                            callFunc();
                    ""","successful"],
                    ["""while(mood == "happy"){
                            study();
                    }""","successful"],

                    # Testcase 248 - 255: do-while
                    ["""do{sleep();}
                        while(everybodyStudying());""","successful"],
                    ["""do{
                            study();
                            eat();
                            x = 1;
                    }while(everybodySleeping());""","successful"],
                    ["""do{
                            x = x + 1;
                    }while (x<100);""","successful"],
                    ["""do{
                            dostuff();
                    }
                    while(homeAlone == true);""","successful"],
                    ["""do{
                            toInfinity();
                    }while(flag == true); ""","successful"],
                    ["""do{
                        laugh();
                        eat();
                        hehe = 123;
                    } while(hotFood);""","successful"],
                    ["""do{
                        takeExercise();
                        x = a + b;
                        print(x);
                    }while(systemLoading);""","successful"],
                    ["""do{
                        wakeUp();

                    }while(!troiToi);""","successful"],

                    # Testcase 256 - 263: Break statement
                    ["""for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            break;
                    }""","successful"],
                    ["""while(i<100){
                        print(i);
                        if(i==a)
                            break;
                    }""","successful"],
                    ["""do{
                            print(i);
                            if(i==a)
                                break;
                    }while(i<100);""","successful"],
                    ["""for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            break;
                    }""","successful"],
                    ["""while(x<100){
                        print(x);
                        if(x==a)
                            break;
                    }""","successful"],
                    ["""do{
                            print(x);
                            if(x==a)
                                break;
                    }while(y<100);""","successful"],
                    ["""for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            break;
                    }""","successful"],
                    ["""while(y<100){
                        print(y);
                        if(y==a)
                            break;
                    }""","successful"],

                    # Testcase 264 - 271: Continue statement
                    ["""for(i=1,i<100,i+1){
                        print(i);
                        if(i == a)
                            continue;
                    }""","successful"],
                    ["""while(i<100){
                        print(i);
                        if(i==a)
                            continue;
                    }""","successful"],
                    ["""do{
                            print(i);
                            if(i==a)
                                continue;
                    }while(i<100);""","successful"],
                    ["""for(x=1,x<100,x+1){
                        print(x);
                        if(x == a)
                            continue;
                    }""","successful"],
                    ["""while(x<100){
                        print(x);
                        if(x==a)
                            continue;
                    }""","successful"],
                    ["""do{
                            print(x);
                            if(x==a)
                                continue;
                    }while(y<100);""","successful"],
                    ["""for(y=1,y<100,y+1){
                        print(y);
                        if(y == a)
                            continue;
                    }""","successful"],
                    ["""while(y<100){
                        print(y);
                        if(y==a)
                            continue;
                    }""","successful"],

                    # Testcase 272 - 279: Return statement:
                    ["""intFunc1: function integer(a: integer, b:integer){
                        return a + b;
                    }""","successful"],
                    ["""floatFunc1: function float(a: float, b:float){
                        return a * b;
                    }""","successful"],
                    ["""autoFunc1: function auto(a: string, b: string){
                        return a::b;
                    }""","successful"],
                    ["""intFunc2: function integer(a: integer, b:integer){
                        return a + b;
                    }""","successful"],
                    ["""floatFunc2: function float(a: float, b:float){
                        return a * b;
                    }""","successful"],
                    ["""autoFunc2: function auto(a: string, b: string){
                        return a::b;
                    }""","successful"],
                    ["""intFunc3: function integer(a: integer, b:integer){
                        return a + b;
                    }""","successful"],
                    ["""floatFunc3: function float(a: float, b:float){
                        return a * b;
                    }""","successful"],

                    # Testcase 280 - 287: Call statement:
                    ["""addAndPrint(a,b);""","successful"],
                    ["""mulAndPrint(a,b);""","successful"],
                    ["""subAndPrint(a,b);""","successful"],
                    ["""divAndPrint(a,b);""","successful"],
                    ["""print("kha dep trai");""","successful"],
                    ["""goo();""","successful"],
                    ["""printFraction(2,3);""","successful"],
                    ["""sleep();""","successful"],

                    # Testcase 288 - 295: Block statement:
                    ["""{
                            doSomething();
                            add();
                            sleep();
                        }""","successful"],
                    ["""{
                            x: integer = 1;
                            a: integer = 2;
                            b: integer;
                            b = a + x;
                        }""","successful"],
                    ["""{
                            add(1,2);
                            sleep();
                        }""","successful"],
                    ["""{
                        if(troiNang == true){
                            rangoaichoi();
                        }
                    }""","successful"],
                    ["""{
                        getCookie();
                        drinkMilk();
                    }""","successful"],
                    ["""{
                        getCookie();
                        drinkMilk();
                    }""","successful"],
                    ["""{
                        print("hehehe", my);
                    }""","successful"],
                    ["""{
                        foo(a,b);
                    }""","successful"],

                    # Testcase 296 - 299: Some syntax error:
                    ["""x:integer = 1""","Error on line 1 col 13: <EOF>"], # forget SEMI at the end of statement
                    ["""add: function int(a: int, b: int){}""",'Error on line 1 col 14: int'], # Type must be "integer", not "int"
                    ["""if(x>2){
                        print("hehehe");
                    """,'Error on line 3 col 20: <EOF>'], # Forget to close block statement
                    ["""a,b,c: integer = 1,2,3,4;""",'Error on line 1 col 22: ,'] # Size of ID list != size of exprlist

                ]

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        testcaseNo = 200
        for testcase in testcaseArray:
            self.assertTrue(TestParser.test(testcase[0], testcase[1], testcaseNo))
            testcaseNo+=1
