using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Desks_Base : MonoBehaviour
{
    private GameObject deskObject;
    public GameObject desk_box;

    private int length = 10;
    public static List<Vector3> desk_list = new List<Vector3>(); // 책상 벡터 저장용
    // Start is called before the first frame update
    void Start()
    {
        deskObject = (GameObject)Resources.Load("Prefabs/Desk");

        for (int i = 0; i != length / 2; ++i)
        {
            for (int j = 0; j != length / 5; ++j)
            {
                desk_box = Instantiate(deskObject);
                desk_box.transform.Translate(i * 10, 0, j * -12);
                desk_box.transform.parent = gameObject.transform;
                desk_list.Add(gameObject.transform.position);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
