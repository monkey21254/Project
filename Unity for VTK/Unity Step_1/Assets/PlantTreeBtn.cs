using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class Ctree
{
    static public string gText = "None";
    static public Vector3 cb_vec_tree = new Vector3();
    static public int[] tree_flags = new int[] {0, 0, 0, 0}; // 상하좌우 flag 설정 ※ 세로 및 가로 최대: 9, 2
    static public int total_tree_count = 0; // 전체 나무 개수 카운트
}

// Cylinder Class
public class CylinderClass //: GameObject
{
    // 변수 지정
    //private GameObject testObject;
    //public GameObject test_box;
    //private GameObject textObject;
    //public GameObject text_box;
    private GameObject boxObject;
    public GameObject obj_box;
    
    public static int cylinder_name = 0; // 이름 용도

    private float for_count;
    //private Vector3 vector_init = new Vector3(0, 0, 0);
    //private Vector3 vector_init2 = new Vector3(0, 0, 0);
    private Vector3 vector_init3 = new Vector3(0, 0, 0);
    //public static List<Vector3> vector_list = new List<Vector3>();
    //public static List<Vector3> vector_list2 = new List<Vector3>();
    public static List<Vector3> vector_list3 = new List<Vector3>();

    // 싱글톤 패턴
    //public static CylinderClass cylinder_obj = new CylinderClass((GameObject)Resources.Load("Prefabs/Cylinder 1"), (GameObject)Resources.Load("Prefabs/CylinderText"));

    // 메소드
    private void getIndex() { ++CylinderClass.cylinder_name; }
    private void setPosition()
    {
        for_count = (Ctree.total_tree_count - 1) * 10;
        
        //// cylinder
        //vector_init.x = for_count - 30;
        //vector_init.y = 6;
        //vector_init.z = -20;
        //// text
        //vector_init2.x = for_count - 30;
        //vector_init2.y = 6;
        //vector_init2.z = -20;
        // Tree
        vector_init3.x = for_count - 30;
        vector_init3.y = 3;
        vector_init3.z = 20;

        //this.test_box.transform.position = vector_init;
        //this.text_box.transform.position = vector_init2;
        this.obj_box.transform.position = vector_init3;

        //vector_list.Add(vector_init);
        //vector_list2.Add(vector_init2);
        vector_list3.Add(vector_init3);
    }

    // 생성자
    //public CylinderClass(GameObject testObject, GameObject textObject, GameObject boxObject)
    public CylinderClass(GameObject boxObject)
    {
        //this.testObject = testObject;
        //this.test_box = MonoBehaviour.Instantiate(this.testObject);
        //this.textObject = textObject;
        //this.text_box = MonoBehaviour.Instantiate(this.textObject);
        this.boxObject = boxObject;
        this.obj_box = MonoBehaviour.Instantiate(this.boxObject);

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
    public static List<GameObject> test_box_list = new List<GameObject>(); // 리스트 생성
    public GameObject textObject;
    public GameObject text_box;
    public static List<GameObject> text_box_list = new List<GameObject>(); // 리스트 생성
    */

    // Cylinder Class
    public CylinderClass custom_cylinder;
    public static List<CylinderClass> cylinder_list = new List<CylinderClass>();

    // Tree
    /*
    public GameObject boxObject;
    public static GameObject obj_box; // obj: Tree, obj2: Text
    public static List<GameObject> obj_box_list = new List<GameObject>(); // 리스트 생성
    */

    // Rotate
    public float mX = 0, mZ = 0;

    // Start is called before the first frame update
    void Start()
    {
        ++Ctree.total_tree_count;

        // ------------------------------- Tree
        //boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup"); // 시작 시 기본 생성 나무
        //obj_box = Instantiate(boxObject); // , transform
        //obj_box.transform.Translate(0, 0, 0);
        //obj_list.Add(obj); // List Start 원소 추가

        //Ctree.cb_vec_tree = obj_box.transform.position;
        //Ctree.gText = Ctree.cb_vec_tree.ToString();
        //Debug.Log(Ctree.cb_vec_tree);

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
        //custom_cylinder = new CylinderClass((GameObject)Resources.Load("Prefabs/Cylinder 1"), (GameObject)Resources.Load("Prefabs/CylinderText"), (GameObject)Resources.Load("Prefabs/TreeGroup"));
        custom_cylinder = new CylinderClass((GameObject)Resources.Load("Prefabs/TreeGroup"));
        cylinder_list.Add(custom_cylinder);

        //Debug.Log(CylinderClass.cylinder_name);
    }
    
    // Update is called once per frame
    void Update()
    {
        //mX += Time.deltaTime * 20.0f;
        //transform.rotation = Quaternion.Euler(mX, 0, 0);

        mX = .005f;
        transform.Rotate(new Vector3(mX, 0, 0));
    }
    
    void OnMouseDown()
    {
        ++Ctree.total_tree_count;
        // ------------------------------- Tree
        //boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup");
        //obj_box = Instantiate(boxObject);
        //obj_box.transform.Translate((Ctree.total_tree_count - 1) * 10, 0, 0);
        //obj_list.Add(obj); // List Update 원소 추가

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
        try
        {
            if ((Ctree.total_tree_count <= 50) == false)
            {
                throw new Exception("Out of Range error....");
            }
            else
            {
                custom_cylinder = new CylinderClass((GameObject)Resources.Load("Prefabs/TreeGroup"));
                cylinder_list.Add(custom_cylinder);
            }
        }
        catch (Exception e)
        {
            Debug.LogError(e);
        }

        Debug.Log(CylinderClass.cylinder_name);
    }
    
    void OnMouseUp()
    {
        //Debug.Log("PlantTreeBtn_OnMouseUp");
    }

    private void OnMouseDrag()
    {
        //Debug.Log("OnMouseDrag in TreeBoxBtn");
        mZ = 1.0f;
        transform.Rotate(new Vector3(0, 0, mZ));
    }

    void OnDestroy()
    {
        //Debug.Log("PlantTreeBtn_OnDestroy");
    }
}
