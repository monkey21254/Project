using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_Btn : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        TextMesh tm = GetComponentInChildren<TextMesh>();
        tm.text = "Create Btn";
        tm.transform.Translate(0, 1, 0);
    }

    // Update is called once per frame
    void Update()
    {

    }
}
