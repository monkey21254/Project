using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Ctree
{
    static public string gText = "None";
    static public Vector3 cb_vec_tree = new Vector3();
    static public int[] tree_flags = new int[] {0, 0, 0, 0}; // �����¿� flag ���� �� ���� �� ���� �ִ�: 9, 2
    static public int total_tree_count = 0; // ��ü ���� ���� ī��Ʈ
}

// Cylinder Class
public class CylinderClass //: GameObject
{
    // ���� ����
    private GameObject testObject;
    public GameObject test_box;
    private GameObject textObject;
    public GameObject text_box;
    public static int cylinder_name = 0; // �̸� �뵵

    private float for_count;
    private Vector3 vector_init = new Vector3(0, 0, 0);
    private Vector3 vector_init2 = new Vector3(0, 0, 0);
    public static List<Vector3> vector_list = new List<Vector3>();
    public static List<Vector3> vector_list2 = new List<Vector3>();

    // �̱��� ����
    //public static CylinderClass cylinder_obj = new CylinderClass((GameObject)Resources.Load("Prefabs/Cylinder 1"), (GameObject)Resources.Load("Prefabs/CylinderText"));

    // �޼ҵ�
    private void getIndex() { ++CylinderClass.cylinder_name; }
    private void setPosition()
    {
        for_count = (Ctree.total_tree_count - 1) * 10;
        
        // cylinder
        vector_init.x = for_count - 30;
        vector_init.y = 6;
        vector_init.z = -20;
        // text
        vector_init2.x = for_count - 30;
        vector_init2.y = 6;
        vector_init2.z = -20;

        this.test_box.transform.position = vector_init; this.text_box.transform.position = vector_init2;
        vector_list.Add(vector_init);
        vector_list2.Add(vector_init2);
    }

    // ������
    public CylinderClass(GameObject testObject, GameObject textObject)
    {
        this.testObject = testObject;
        this.test_box = MonoBehaviour.Instantiate(this.testObject);
        this.textObject = textObject;
        this.text_box = MonoBehaviour.Instantiate(this.textObject);
        this.getIndex();
        this.setPosition();

    }
}

public class PlantTreeBtn : MonoBehaviour
{
    // Cylinder
    /*
    public GameObject testObject;
    public GameObject test_box;
    public static List<GameObject> test_box_list = new List<GameObject>(); // ����Ʈ ����
    public GameObject textObject;
    public GameObject text_box;
    public static List<GameObject> text_box_list = new List<GameObject>(); // ����Ʈ ����
    */

    // Cylinder Class
    public CylinderClass custom_cylinder;
    public static List<CylinderClass> cylinder_list = new List<CylinderClass>();
    public static List<int> index_list = new List<int>(); // Ư���� �ε����� �����ؼ� destroy�� �ϱ� ���� �뵵�� ���� ���Դϴ�.


    // Tree
    public GameObject boxObject;
    public static GameObject obj_box; // obj: Tree, obj2: Text
    public static List<GameObject> obj_box_list = new List<GameObject>(); // ����Ʈ ����


    // Start is called before the first frame update
    void Start()
    {
        ++Ctree.total_tree_count;

        // ------------------------------- Tree
        boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup"); // ���� �� �⺻ ���� ����
        obj_box = Instantiate(boxObject); // , transform
        obj_box.transform.Translate(0, 0, 0);
        //obj_list.Add(obj); // List Start ���� �߰�

        Ctree.cb_vec_tree = obj_box.transform.position;
        Ctree.gText = Ctree.cb_vec_tree.ToString();
        Debug.Log(Ctree.cb_vec_tree);

        // ------------------------------- Cylinder
        /*
        testObject = (GameObject)Resources.Load("Prefabs/Cylinder 1");
        test_box = Instantiate(testObject); // , transform
        test_box.transform.Translate(-30, 0, -20);
        test_box_list.Add(test_box);

        textObject = (GameObject)Resources.Load("Prefabs/CylinderText");
        text_box = Instantiate(textObject); // , transform
        text_box.transform.Translate(0, 0, 0);
        text_box_list.Add(text_box);
        */

        // ------------------------------- CylinderClass
        custom_cylinder = new CylinderClass((GameObject)Resources.Load("Prefabs/Cylinder 1"), (GameObject)Resources.Load("Prefabs/CylinderText"));
        cylinder_list.Add(custom_cylinder);
        index_list.Add(Ctree.total_tree_count);


        Debug.Log(CylinderClass.cylinder_name);
    }
    
    // Update is called once per frame
    void Update()
    {

    }
    
    void OnMouseDown()
    {
        if(obj_box != null)
        {
            ++Ctree.total_tree_count;
            // ------------------------------- Tree
            boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup");
            obj_box = Instantiate(boxObject);
            obj_box.transform.Translate((Ctree.total_tree_count - 1) * 10, 0, 0);
            //obj_list.Add(obj); // List Update ���� �߰�

            //Ctree.cb_vec_tree = obj.transform.position;
            //Ctree.gText = Ctree.cb_vec_tree.ToString();

            // ------------------------------- Cylinder
            /*
            testObject = (GameObject)Resources.Load("Prefabs/Cylinder 1");
            test_box = Instantiate(testObject); // , transform
            test_box.transform.Translate((Ctree.total_tree_count - 1) * 10 - 30, 0, -20);
            test_box_list.Add(test_box);

            textObject = (GameObject)Resources.Load("Prefabs/CylinderText");
            text_box = Instantiate(textObject); // , transform
            text_box.transform.Translate(0, 0, (Ctree.total_tree_count - 1) * 10);
            text_box_list.Add(text_box);

            Debug.Log(text_box_list.Count);
            */

            // ------------------------------- Cylinder Class
            custom_cylinder = new CylinderClass((GameObject)Resources.Load("Prefabs/Cylinder 1"), (GameObject)Resources.Load("Prefabs/CylinderText"));
            cylinder_list.Add(custom_cylinder);
            index_list.Add(Ctree.total_tree_count);


            Debug.Log(CylinderClass.cylinder_name);
        }

    }
    
    void OnMouseUp()
    {
        //Debug.Log("PlantTreeBtn_OnMouseUp");
    }

    void OnDestroy()
    {
        //Debug.Log("PlantTreeBtn_OnDestroy");
    }
}
