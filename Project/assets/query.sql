SELECT
    d.sw,
    d.bodega,
    d.fecha,
    d.vendedor AS ident_asesor,
    tv.nombres AS nom_asesor,
    d.nit AS ident_cliente,
    t.nombres AS nom_cliente,
    CASE
        WHEN d.sw = 1 
            THEN a.cantidad 
            ELSE (a.cantidad) * -1
    END AS cantidad,
    CASE
        WHEN d.sw = 1 
            THEN CONVERT(MONEY, a.costo_unitario) 
            ELSE CONVERT(MONEY, a.costo_unitario) * -1
    END AS costo_unitario,
    CASE
        WHEN d.sw = 1 
            THEN CONVERT(MONEY, (CONVERT(MONEY, a.valor_unitario - (a.valor_unitario * a.porcentaje_descuento) / 100) - a.costo_unitario)) 
            ELSE CONVERT(MONEY, (CONVERT(MONEY, a.valor_unitario - (a.valor_unitario * a.porcentaje_descuento) / 100) - a.costo_unitario)) * -1
    END AS utilidad,
    v.modelo,
    v.des_modelo,
    ISNULL(tf.nombres, 'NA') AS financiera,
    dias_inv = (
        SELECT TOP 1 ABS(DATEDIFF(DAY, l.fec, d.fecha))
        FROM documentos_lin l
        WHERE a.codigo = l.codigo
            AND l.sw IN (2, 3)
            AND l.tipo IN ('FCM', 'SII')
    ),
    ISNULL(vc.descripcion, 'DEV') AS clasificacion,
    doc_ref = (d.prefijo + '/' + d.documento)
FROM documentos d
JOIN documentos_lin a ON d.tipo = a.tipo
    AND d.numero = a.numero
LEFT JOIN terceros t ON d.nit = t.nit
LEFT JOIN y_ciudades yc ON t.y_ciudad = yc.ciudad
    AND t.y_dpto = yc.departamento
LEFT JOIN terceros tv ON d.vendedor = tv.nit
LEFT JOIN v_vh_vehiculos v ON a.codigo = v.codigo
LEFT JOIN vh_documentos_ped vp ON d.tipo = vp.tipo_factura
    AND d.numero = vp.factura
    AND a.codigo = vp.codigo
LEFT JOIN terceros tf ON vp.nit_prenda = tf.nit
LEFT JOIN vh_clasificacion vc ON vp.clasificacion = vc.clasificacion
LEFT JOIN v_referencias_fis rf ON a.codigo = rf.codigo
    AND a.bodega = rf.bodega
LEFT JOIN vh_modelo vm ON v.modelo = vm.modelo
WHERE d.sw IN (1, 2)
    AND (d.tipo LIKE ('FM%') OR d.tipo LIKE ('DM%'))
    AND d.anulado = 0
    AND d.bodega >= 2004
    --AND d.fecha >= DATEADD(MM, DATEDIFF(MM, 0, GETDATE()), 0)
    AND fec <= DATEADD(DAY, 0, GETDATE())
ORDER BY d.fecha
