using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_3 : MonoBehaviour
{
    public TextMesh mTm3;
    public float x, y, z;
    // Start is called before the first frame update
    void Start()
    {
        mTm3 = GetComponent<TextMesh>();
    }

    // Update is called once per frame
    void Update()
    {
        mTm3.text = Cb3.gText;
        transform.position = Cb3.cb_vec3;
        x = transform.position.x;
        y = transform.position.y;
        z = transform.position.z;
        transform.position = new Vector3(x, y - 1, z);
    }
}
