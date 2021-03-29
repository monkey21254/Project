using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DeskClass
{
    public static List<Vector3> vec3_desk_sumlist = new List<Vector3>(); // ��ο� ����Ʈ

    // �߰����� üũ �뵵
    public static Vector3 middle_point = new Vector3(-30, 1.5f, -10);
    public static Vector3 middle_point1 = new Vector3(-17, 1.5f, -10);
    public static Vector3 middle_point2 = new Vector3(-17, 1.5f, 0);
    public static Vector3 middle_point3 = new Vector3(-17, 1.5f, 11);
    //public static int cnt = 0;

    public static void from_start_to_middle()
    // _gameObject_dst: ���������� å��                               , flag_num: �̵������ ������ ����ġ.
    {
        if (DeskClass.vec3_desk_sumlist.Count >= 1)
        {
            DeskClass.vec3_desk_sumlist.Clear();
        }

        BeaconBtn.students_list[Students.student_index].student_box.transform.Translate(0, -3, 0);

        int cnt = 0;
        DeskClass.vec3_desk_sumlist.Add(BeaconBtn.students_list[Students.student_index].student_box.transform.position);
        ++cnt;
        DeskClass.vec3_desk_sumlist.Insert(cnt, DeskClass.vec3_desk_sumlist[0] + new Vector3(0, 0, 2));
        ++cnt;
        DeskClass.vec3_desk_sumlist.Insert(cnt, new Vector3(DeskClass.middle_point.x, DeskClass.vec3_desk_sumlist[cnt - 1].y, DeskClass.vec3_desk_sumlist[cnt - 1].z));
        ++cnt;
        DeskClass.vec3_desk_sumlist.Insert(cnt, DeskClass.middle_point);
        ++cnt;

        // �ٸ� å�� ������Ʈ���� �÷��׸� üũ�ؼ� ��ο� �־�� �Ѵ�. + ����ũ ������Ʈ�� ��ġ�� �������� ������ �־� �߽����� �ٸ��� �⵵�� �ؾ� �Ѵ�.
    }
}


public class Desks_Base : MonoBehaviour
{
    private GameObject deskObject;
    public GameObject desk_box;
    private int length = 10;

    public DeskClass custom_desks;
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
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
