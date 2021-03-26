using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq; // enumerate + lambda 활용.
using System.Diagnostics;


public class TreeBox_default : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

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

        // ------------------------------- Cylinder Class + 시간 측정
        //Destroy(PlantTreeBtn.cylinder_list[CylinderClass.cylinder_name - 1]); // 상속 및 derive 오류 해결 필요.

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        for (int i = 0; i != PlantTreeBtn.cylinder_list.Count; ++i)
        {
            if (PlantTreeBtn.cylinder_list[i].obj_box == gameObject)
            {
                //Destroy(PlantTreeBtn.cylinder_list[i].test_box);
                //Destroy(PlantTreeBtn.cylinder_list[i].text_box);
                Destroy(PlantTreeBtn.cylinder_list[i].obj_box);
                PlantTreeBtn.cylinder_list.RemoveAt(i);
                break;
            }
        }

        sw.Stop();
        // UnityEngine & Diagnostic Debug 충돌 이슈
        UnityEngine.Debug.Log("ElapsedMilliseconds: " + sw.ElapsedMilliseconds.ToString() + "ms");

        --Ctree.total_tree_count;
        //CylinderClass.vector_list.RemoveAt(Ctree.total_tree_count);
        //CylinderClass.vector_list2.RemoveAt(Ctree.total_tree_count);
        CylinderClass.vector_list3.RemoveAt(Ctree.total_tree_count);
        
        // UnityEngine & Diagnostic Debug 충돌 이슈
        UnityEngine.Debug.Log(PlantTreeBtn.cylinder_list.Count);
        foreach (var it in PlantTreeBtn.cylinder_list.Select((Value, Index) => new { Value, Index }))
        {
            //it.Value.test_box.transform.position = CylinderClass.vector_list[it.Index];
            //it.Value.text_box.transform.position = CylinderClass.vector_list2[it.Index];
            it.Value.obj_box.transform.position = CylinderClass.vector_list3[it.Index];

            //Debug.LogFormat("{0}: {1}", it.Index, it.Value);
        }

    }

    void OnMouseUp() {
        //Debug.Log("OnMouseUp");

        /*
        int total_num = 0x3ffFfff;
        List<int> work_time_list = new List<int>();

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        for (int i = 0; i != total_num; ++i)
        {
            work_time_list.Add(i);
        }

        int r1 = work_time_list[total_num];
        int r2 = work_time_list.Find(x1 => x1 == 1357);
        int i1 = work_time_list.FindIndex(x1 => x1 == 2468);
        int i2 = work_time_list.IndexOf(total_num - 500);

        sw.Stop();
        UnityEngine.Debug.Log("ElapsedMilliseconds: " + sw.ElapsedMilliseconds.ToString() + "ms");
        */
    }

    void OnDestroy()
    {
        //Debug.Log("Box_OnDestroy");
    }
}
