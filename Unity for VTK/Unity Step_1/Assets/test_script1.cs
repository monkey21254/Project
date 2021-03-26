using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;


public class test_script1 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //Debug.Log("testScript_Start");
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnMouseDown()
    {
        //Debug.Log("test_script1_OnMouseDown");

        // ------------------------------- Cylinder
        /*
        Debug.Log(PlantTreeBtn.test_box_list.Count);
        Destroy(PlantTreeBtn.test_box_list[Ctree.total_tree_count - 1]);
        Destroy(PlantTreeBtn.text_box_list[Ctree.total_tree_count - 1]);
        PlantTreeBtn.test_box_list.RemoveAt(Ctree.total_tree_count - 1);
        PlantTreeBtn.text_box_list.RemoveAt(Ctree.total_tree_count - 1);

        foreach (GameObject item in PlantTreeBtn.test_box_list)
        {
            Debug.Log(item);
        }
        */

        // ------------------------------- Cylinder Class
        //Destroy(PlantTreeBtn.cylinder_list[CylinderClass.cylinder_name - 1]); // 상속 및 derive 오류 해결 필요.


        //for (int i = 0; i != PlantTreeBtn.cylinder_list.Count; ++i)
        //{
        //    if (PlantTreeBtn.cylinder_list[i].test_box == gameObject)
        //    {
        //        Destroy(PlantTreeBtn.cylinder_list[i].test_box);
        //        Destroy(PlantTreeBtn.cylinder_list[i].text_box);
        //        Destroy(PlantTreeBtn.cylinder_list[i].obj_box);
        //        PlantTreeBtn.cylinder_list.RemoveAt(i);
        //        break;
        //    }
        //}

        //--Ctree.total_tree_count;
        //CylinderClass.vector_list.RemoveAt(Ctree.total_tree_count);
        //CylinderClass.vector_list2.RemoveAt(Ctree.total_tree_count);
        //CylinderClass.vector_list3.RemoveAt(Ctree.total_tree_count);

        //Debug.Log(PlantTreeBtn.cylinder_list.Count);
        //foreach (var it in PlantTreeBtn.cylinder_list.Select((Value, Index) => new { Value, Index }))
        //{
        //    it.Value.test_box.transform.position = CylinderClass.vector_list[it.Index];
        //    it.Value.text_box.transform.position = CylinderClass.vector_list2[it.Index];
        //    it.Value.obj_box.transform.position = CylinderClass.vector_list3[it.Index];
        //    //Debug.LogFormat("{0}: {1}", it.Index, it.Value);
        //}
    }


    void OnMouseUp()
    {
        //Debug.Log("test_script1_OnMouseUp");
    }
}
