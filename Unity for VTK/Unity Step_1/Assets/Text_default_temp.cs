using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_group : MonoBehaviour
{
    // List

    //public List<TextMesh> mTm_list;
    public TextMesh mTm_group;
    public int text_count;
    // Start is called before the first frame update
    void Start()
    {
        mTm_group = GetComponent<TextMesh>();
        //text_count = 0; // 최대 10억개

        mTm_group.text = Ctree.total_tree_count.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 temp = new Vector3();
        
        temp.x = Ctree.cb_vec_tree.x;
        temp.y = Ctree.cb_vec_tree.y + 15;
        temp.z = Ctree.cb_vec_tree.z;
        //transform.position = temp;

        //mTm_group.text = Ctree.total_tree_count.ToString();

        //Debug.Log(Ctree.cb_vec_tree);
    }


    void OnMouseDown()
    {
        //Destroy(PlantTreeBtn.obj2);
        //Destroy(PlantTreeBtn.obj);

        Debug.Log("OnMouseDown");
    }


    void OnMouseUp()
    {
        Debug.Log("OnMouseUp");
    }


    void OnDestroy()
    {
        //Destroy(PlantTreeBtn.obj2);
    }
}
