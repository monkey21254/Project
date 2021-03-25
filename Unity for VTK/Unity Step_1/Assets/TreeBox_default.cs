using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class TreeBox_default : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
        //Debug.Log(tree_test);
        //Debug.Log(text_test);

        //Debug.Log("TreeBox_default");
    }

    // Update is called once per frame
    void Update()
    {
        
    }


    void OnMouseDown()
    {
        Debug.Log("TreeBox_Destroy");
    }

    void OnMouseUp() {
        Debug.Log("OnMouseUp");
    }

    void OnDestroy()
    {
        //Debug.Log("Box_OnDestroy");
    }
}
