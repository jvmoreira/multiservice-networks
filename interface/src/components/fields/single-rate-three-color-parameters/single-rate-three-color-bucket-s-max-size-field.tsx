import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorBucketSMaxSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorBucketSMaxSize = useMemo(() => {
    return singleRateThreeColorParameters.bucketS_max_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketSMaxSize = useSetNfvTeFunctionParameter('bucketS_max_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketSMaxSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketSMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket E"
      name="bucket-s-max-size"
      value={singleRateThreeColorBucketSMaxSize}
      placeholder="Valor em tokens"
      onChange={onSingleRateThreeColorBucketSMaxSizeChangeHandler}
    />
  );
}
