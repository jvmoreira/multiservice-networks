import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorBucketFMaxSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorBucketFMaxSize = useMemo(() => {
    return singleRateThreeColorParameters.bucketF_max_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketFMaxSize = useSetNfvTeFunctionParameter('bucketF_max_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketFMaxSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketFMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket C"
      name="bucket-f-max-size"
      value={singleRateThreeColorBucketFMaxSize}
      placeholder="Valor em tokens"
      onChange={onSingleRateThreeColorBucketFMaxSizeChangeHandler}
    />
  );
}
