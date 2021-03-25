using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cylinder_text : MonoBehaviour
{
    public TextMesh mTm_group;
    // Start is called before the first frame update
    void Start()
    {
        mTm_group = GetComponent<TextMesh>();
        mTm_group.text = Ctree.total_tree_count.ToString();

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
