using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Ctree
{
    static public string gText = "None";
    static public Vector3 cb_vec_tree = new Vector3();
    static public List<int> tree_flags = new List<int> {0, 0, 0, 0}; // 상하좌우 flag 설정 ※ 세로 및 가로 최대: 9, 2
    static public int total_tree_count = 0; // 전체 나무 개수 카운트
}


public class PlantTreeBtn : MonoBehaviour
{
    public static GameObject boxObject;
    public static GameObject obj_box; // obj: Tree, obj2: Text
    public List<GameObject> obj_box_list; // 리스트 생성
    // Start is called before the first frame update
    void Start()
    {
        Ctree.total_tree_count += 1;
        boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup"); // 시작 시 기본 생성 나무
        obj_box = Instantiate(boxObject); // , transform
        obj_box.transform.Translate(-30, 3, 20);
        Ctree.cb_vec_tree = obj_box.transform.position;
        Ctree.gText = Ctree.cb_vec_tree.ToString();
        
        //obj_list.Add(obj); // List Start 원소 추가

        Debug.Log(Ctree.cb_vec_tree);
    }
    
    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseDown()
    {
        if(obj_box != null) // Tree
        {
            Ctree.total_tree_count += 1;
            boxObject = (GameObject)Resources.Load("Prefabs/TreeGroup");
            obj_box = Instantiate(boxObject);
            obj_box.transform.Translate((Ctree.total_tree_count - 1) * 10 - 30, 3, 20);

            //obj_list.Add(obj); // List Update 원소 추가


            //Ctree.cb_vec_tree = obj.transform.position;
            //Ctree.gText = Ctree.cb_vec_tree.ToString();
        }
    }
    
    void OnMouseUp()
    {
        //Debug.Log("OnMouseUp");
    }

    void OnDestroy()
    {
        Destroy(obj_box);
    }
}
