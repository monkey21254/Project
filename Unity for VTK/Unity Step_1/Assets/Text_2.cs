using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_2 : MonoBehaviour
{
    public TextMesh mTm2;
    public float x, y, z;
    // Start is called before the first frame update
    void Start()
    {
        mTm2 = GetComponent<TextMesh>();
    }

    // Update is called once per frame
    void Update()
    {
        mTm2.text = Cb2.gText;
        transform.position = Cb2.cb_vec2;
        x = transform.position.x;
        y = transform.position.y;
        z = transform.position.z;
        transform.position = new Vector3(x, y - 1, z);
    }
}
