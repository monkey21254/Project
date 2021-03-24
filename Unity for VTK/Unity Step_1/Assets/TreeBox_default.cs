using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TreeBox_default : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Start" + Ctree.total_tree_count.ToString());
    }

    // Update is called once per frame
    void Update()
    {
        
    }


    void OnMouseDown()
    {
        Debug.Log("test");
        Destroy(this);
    }

    void OnDestroy()
    {
        Destroy(this);
    }
}
