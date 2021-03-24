using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Tree_default : MonoBehaviour
{
    public GameObject boxObject;
    public static GameObject obj_box;
    public static List<GameObject> obj_box_list;
    // Start is called before the first frame update
    void Start()
    {
        //boxObject = (GameObject)Resources.Load("Prefabs/Text_group");
        //obj2 = Instantiate(boxObject);
        //obj2.transform.Translate(-15, 15, (Ctree.total_tree_count - 1) * 10 - 35);
    }
    

    // Update is called once per frame
    void Update()
    {
        
    }


    void OnMouseDown()
    {
        //Destroy(obj2);
        //Destroy(PlantTreeBtn.obj);

        Debug.Log("OnMouseDown");
    }


    void OnMouseUp()
    {
        Debug.Log("OnMouseUp");
    }


    void OnDestroy()
    {
        //Destroy(PlantTreeBtn.obj);
    }
}
